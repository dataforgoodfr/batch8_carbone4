# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
#import fonctions as fn

# Chargement des données
echantillon_df = pd.read_csv("data/C4_OandG.csv") 

# Dictionnaire stockant les noms de variable pour les abscisses
x_labels = {"GICS4": "Sector",
                "HQ_SubRegion_ord": "Location",
                "gas_class": "Gas share in the mix",
                "marketCap_class": "Market cap (M€)",
                "vol_class": "Managed volume (toe)",
                #"cat_CA_2019": "Chiffre d'affaires (M€)"
                }

# Dictionnaire stockant les noms de variable pour les ordonnées
y_labels = {"nombre_entreprises": "Number of companies",
                #"total_induced": "Émissions induites totales",
                #"capitalisation_boursiere_2019": "Capitalisation boursière (M€)",
                #"CA_2019": "Chiffre d'affaires (M€)",
                #"volume_total_gere": "Volume géré (toe)"
                }

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("X variable"),
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
                dbc.Label("Y variable"),
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
            dbc.Col(html.H2('Sector "Oil & Gas" companies analysed by Carbon4Finance'))
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col([
                    html.Div("Companies"),
                    html.H3("96"),
                ]),
                dbc.Col([
                    html.Div("Analysed in"),
                    html.H3("2019"),
                ]),
                dbc.Col([
                    html.Div("Induced emissions"),
                    html.H3("34%"),
                    html.Div("of global emissions"),
                    html.Div("(= 33,5 Gt CO2)"),
                ]),
                dbc.Col([
                    html.Br(),
                    html.H3("61%"),
                    html.Div("of global emissions due to oil and gas (= 18,5 Gt CO2)"),
                ]),
                dbc.Col([
                    html.Div("Managed total volume"),
                    html.H3("41%"),
                    html.Div("of oil and gas global volume (= 7,8 Gtoe)"),
                ]),
                dbc.Col([
                    html.Div("Market cap"),
                    html.H3("78%"),
                    html.Div("of the sector"),
                    html.Div("(= 5,2 KB€)"),
                ]),
                dbc.Col([
                    html.Div("Revenue"),
                    html.H3("60%"),
                    html.Div("of the sector"),
                    html.Div("(= 5,3 KB€)"),
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
        return [{"label": "Sum", "value": "somme"}, {"label": "Log", "value": "log"}]
    else:
        return [{"label": "Unavailable", "value": "indisponible", "disabled": True}]


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
        table = gb["Company_Name"].count()

        # Mise en forme de la table précédente pour un bel affichage sur la visualisation
        table_finale = pd.concat([table], axis=1)
        table_finale.columns = [y_labels[nom_variable_y]] # on renomme le nom de la colonne (le nombre d'entreprises) par son label
        table_finale.index.name = x_labels[nom_variable_x] # de même pour l'index (la variable X sélectionnée)
        table_finale.sort_values(by=x_labels[nom_variable_x], ascending=True, inplace=True)

        fig = px.bar(table_finale, y=y_labels[nom_variable_y], text=y_labels[nom_variable_y], height=550)

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

        fig = px.bar(table_finale, y=y_labels[nom_variable_y], text=y_labels[nom_variable_y], height=550)

        fig.update_traces(textposition='outside')

    else:

        fig = px.box(echantillon_df, x=nom_variable_x, y=nom_variable_y, 
                    labels={nom_variable_x: x_labels[nom_variable_x], nom_variable_y: y_labels[nom_variable_y]},
                    log_y=True)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
