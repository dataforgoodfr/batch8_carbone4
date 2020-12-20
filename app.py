# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import collections
from dash.dependencies import Input, Output
#import fonctions as fn

# Chargement des données
echantillon_df = pd.read_csv("data/C4_OandG_v6.csv")

# Describe the order in each category
category_items = {
	"GICS4": [
        'Oil & Gas Exploration & Production',
        'Oil & Gas Refining & Marketing',
	    'Oil & Gas Storage & Transportation',
        'Gas Utilities',
        'Integrated Oil & Gas',
	],
	"HQ_SubRegion_ord":[
		'Northern America',
		'Latin America',
		'Northern Europe',
		'Western Europe',
		'Southern Europe',
		'Eastern Europe',
		'Western Asia',
		'Southern Asia',
		'Southeastern Asia',
		'Eastern Asia',
		'Western Africa',
		'Middle Africa',
		'Melanesia',
		'Australasia',
	],
	"marketCap_class":[
		'Company not quoted',
	    '0 MEUR < market cap < 1,000 MEUR',
		'1,000 MEUR<= market cap < 10,000 MEUR',
	    '10,000 MEUR<= market cap < 100,000 MEUR',
	    'Market cap >= 100,000 MEUR'
	],
    "vol_class":[
    '0 Mtoe <= Volume managed < 5 Mtoe',
    '5 Mtoe <= Volume managed < 10 Mtoe',
    '10 Mtoe <= Volume managed < 27 Mtoe',
    'Volume managed >= 27 Mtoe'
    ],
    "gas_class":[
	'No gas',
	'0%<gas in the mix<33%',
	'33%<=gas in the mix<67%',
    '67%<=gas in the mix<100%',
    'Only gas',
	 ],
}


# Dictionnaire stockant les noms de variable pour les abscisses
x_labels = {"GICS4": "Sector",
                "HQ_SubRegion_ord": "Location",
                "gas_class": "Gas share in the mix",
                "marketCap_class": "Market cap (M€)",
                "vol_class": "Managed volume (toe)",
                #"cat_CA_2019": "Chiffre d'affaires (M€)"
                }

# Dictionnaire stockant les noms de variable pour les ordonnées
y_labels = {"nombre_entreprises": "Count of companies",
            "total_induced": "Total induced emisions (teqCO2)",
            "Market_cap": "Market capitalisation (M€)",
            "revenues_mEUR_2019": "Revenue (M€)",
            "vol": "Managed volume (toe)"
            }

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Select a category"),
                dcc.Dropdown(
                    id="x-variable",
                    options=[
                        {"label": x_labels[nom_variable], "value": nom_variable} for nom_variable in x_labels
                    ],
                    value="GICS4"
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Select a variable"),
                dcc.Dropdown(
                    id="y-variable",
                    options=[
                       {"label": y_labels[nom_variable], "value": nom_variable} for nom_variable in y_labels
                    ],
                    value="nombre_entreprises"
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Choose the Y display"),
                dbc.RadioItems(id="choix-affichage-y", value="somme")
            ]
        ),
    ],
    body=True,
)


app.layout = dbc.Container([

        dbc.Row(
            dbc.Col(html.H2('Our analyses are based on a representative sample of companies from the Oil & Gas (O&G) sector.'))
        ),
        html.Hr(),
        #dbc.Row(
        #    dbc.Col(html.H4('Percentages below represent the share of our sample on the global O&G sector.'))
        #),
        dbc.Row(
            [
                dbc.Col([
                    html.H3("96"),
                    html.Div("Number of companies"),
                ]),
                dbc.Col([
                    html.H3("2019"),
                    html.Div("Reporting year"),
                ]),
                dbc.Col([
                    html.H3("34%"),
                    html.Div("of the worldwide CO2 emissions (33.5 BT)"),
                ]),
                dbc.Col([
                    html.H3("61%"),
                    html.Div("of the CO2 emissions from the sector (18.5 BT)"),
                ]),
                dbc.Col([
                    html.H3("41%"),
                    html.Div("of the volume managed by the sector (7.8 BT)"),
                ]),
                dbc.Col([
                    html.H3("78%"),
                    html.Div("of the sector market capitalisation (5,200 B€)"),
                ]),
                dbc.Col([
                    html.H3("60%"),
                    html.Div("of the sector total revenue (5,300 B€)"),
                ]),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(controls, md=3),
                dbc.Col(dcc.Graph(id="data-viz"), md=9),
            ],
            align="center"
        ),


    ]
)

@app.callback(
    Output("choix-affichage-y", "options"),
    Input("y-variable", "value")
)
def modifier_options_radio(nom_variable_y):
    if nom_variable_y != "nombre_entreprises":
        return [{"label": "Count", "value": "somme"}, {"label": "Summary statistics", "value": "stats"}]
    else:
        return [{"label": "Not applicable", "value": "indisponible", "disabled": True}]


@app.callback(
    Output("data-viz", "figure"),
    [
        Input("x-variable", "value"),
        Input("y-variable", "value"),
        Input("choix-affichage-y", "value"),
    ],
)
def make_graph(nom_variable_x, nom_variable_y, choix_affichage_y):

    if nom_variable_y == "nombre_entreprises":

        # Nombre d'entreprises selon la variable sélectionnée en X
        gb = echantillon_df.groupby(nom_variable_x)
        table = gb["Company"].count()

        # Mise en forme de la table précédente pour un bel affichage sur la visualisation
        table_finale = pd.concat([table], axis=1)
        table_finale.columns = [y_labels[nom_variable_y]] # on renomme le nom de la colonne (le nombre d'entreprises) par son label
        table_finale.index.name = x_labels[nom_variable_x] # de même pour l'index (la variable X sélectionnée)
        table_finale.sort_values(by=x_labels[nom_variable_x], ascending=True, inplace=True)

        fig = px.bar(table_finale, y=y_labels[nom_variable_y],
        #text=y_labels[nom_variable_y], 
        height=550)

        fig.update_traces(textposition='outside')

    elif choix_affichage_y == "somme":

        # Somme de la variable sélectionnée en Y selon la variable sélectionnée en X
        gb = echantillon_df.groupby(nom_variable_x)
        table = gb[nom_variable_y].sum()

        # Mise en forme de la table précédente pour un bel affichage sur la visualisation
        table_finale = pd.concat([table], axis=1)
        table_finale.columns = [y_labels[nom_variable_y]] # on renomme le nom de la colonne (le nombre d'entreprises) par son label
        table_finale[y_labels[nom_variable_y]] = table_finale[y_labels[nom_variable_y]].apply(round)
        table_finale.index.name = x_labels[nom_variable_x] # de même pour l'index (la variable X sélectionnée)
        table_finale.sort_values(by=x_labels[nom_variable_x], ascending=True, inplace=True)

        fig = px.bar(table_finale, y=y_labels[nom_variable_y],
        #text=y_labels[nom_variable_y],
        height=550)

        fig.update_traces(textposition='outside')

    else:

        fig = px.box(echantillon_df, x=nom_variable_x, y=nom_variable_y,
                    labels={nom_variable_x: x_labels[nom_variable_x], nom_variable_y: y_labels[nom_variable_y]},
                    log_y=True)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
