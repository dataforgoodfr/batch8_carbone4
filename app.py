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
x_variables = {"GICS4": "Secteur d'activité",
                "HQ_SubRegion_ord": "Localisation",
                "gas_class": "Part du gaz dans le mix",
                "marketCap_class": "Capitalisation boursière (M€)",
                "vol_class": "Volume géré (toe)",
                #"cat_CA_2019": "Chiffre d'affaires (M€)"
                }

# Dictionnaire stockant les noms de variable pour les ordonnées
y_variables = {"nombre_entreprises": "Nombre d'entreprises",
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
                        {"label": x_variables[variable], "value": variable} for variable in x_variables
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
                       {"label": y_variables[variable], "value": variable} for variable in y_variables
                    ],
                    value="nombre_entreprises"
                ),
            ]
        ),
    ],
    body=True,
)

app.layout = dbc.Container([

        dbc.Row(
            dbc.Col(html.H2('Entreprises du secteur "Oil & Gas" analysées par Carbone4Finance'))
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col([
                    html.Div("Entreprises"),
                    html.H1("96"),
                ]),
                dbc.Col([
                    html.Div("Analyse sur"),
                    html.H1("2019"),
                ]),
                dbc.Col([
                    html.Div("Émissions induites"),
                    html.H1("34%"),
                    html.Div("des émissions mondiales"),
                ]),
                dbc.Col([
                    html.Br(),
                    html.H1("61%"),
                    html.Div("des émissions mondiales liées au pétrole et au gaz"),
                ]),
                dbc.Col([
                    html.Div("Volume total géré"),
                    html.H1("41%"),
                    html.Div("du volume mondial fourni de pétrole et de gaz"),
                ]),
                dbc.Col([
                    html.Div("Market cap"),
                    html.H1("78%"),
                    html.Div("du secteur"),
                ]),
                dbc.Col([
                    html.Div("CA"),
                    html.H1("60%"),
                    html.Div("du secteur"),
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
    Output("data-viz", "figure"),
    [
        Input("x-variable", "value"),
        Input("y-variable", "value"),
    ],
)
def make_graph(x, y):

    if y != "nombre_entreprises":
        fig = px.box(echantillon_df, x=x, y=y, labels={x: x_variables[x], y: y_variables[y]})
    else:

        # Préparation données pour la visualisation du secteur d'activité
        gb = echantillon_df.groupby(x)
        table = gb["Company_Name"].count()

        table_finale = pd.concat([table], axis=1)
        table_finale.columns = [y_variables[y]]
        table_finale.index.name = x_variables[x]
        table_finale.sort_values(by=x_variables[x], ascending=True, inplace=True)

        fig = px.bar(table_finale, y=y_variables[y], text=y_variables[y])

        fig.update_traces(textposition='outside')

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
