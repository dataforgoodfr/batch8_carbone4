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
x_labels = {"GICS4": "Secteur d'activité",
                "HQ_SubRegion_ord": "Localisation",
                "gas_class": "Part du gaz dans le mix",
                "marketCap_class": "Capitalisation boursière (M€)",
                "vol_class": "Volume géré (toe)",
                #"cat_CA_2019": "Chiffre d'affaires (M€)"
                }

# Dictionnaire stockant les noms de variable pour les ordonnées
y_labels = {"nombre_entreprises": "Nombre d'entreprises",
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
                    html.H3("96"),
                ]),
                dbc.Col([
                    html.Div("Analyse sur"),
                    html.H3("2019"),
                ]),
                dbc.Col([
                    html.Div("Émissions induites"),
                    html.H3("34%"),
                    html.Div("des émissions mondiales"),
                    html.Div("(= 33,5 Gt CO2)"),
                ]),
                dbc.Col([
                    html.Br(),
                    html.H3("61%"),
                    html.Div("des émissions mondiales liées au pétrole et au gaz (= 18,5 Gt CO2)"),
                ]),
                dbc.Col([
                    html.Div("Volume total géré"),
                    html.H3("41%"),
                    html.Div("du volume mondial fourni de pétrole et de gaz (= 7,8 Gtoe)"),
                ]),
                dbc.Col([
                    html.Div("Market cap"),
                    html.H3("78%"),
                    html.Div("du secteur"),
                    html.Div("(= 5,2 KMds€)"),
                ]),
                dbc.Col([
                    html.Div("CA"),
                    html.H3("60%"),
                    html.Div("du secteur"),
                    html.Div("(= 5,3 KMds€)"),
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
def make_graph(nom_variable_x, nom_variable_y):

    if nom_variable_y != "nombre_entreprises":
        fig = px.box(echantillon_df, x=nom_variable_x, y=nom_variable_y, labels={nom_variable_x: x_labels[nom_variable_x], nom_variable_y: y_labels[nom_variable_y]})
    else:

        # Préparation données pour la visualisation du secteur d'activité
        gb = echantillon_df.groupby(nom_variable_x)
        table = gb["Company_Name"].count()

        table_finale = pd.concat([table], axis=1)
        table_finale.columns = [y_labels[nom_variable_y]]
        table_finale.index.name = x_labels[nom_variable_x]
        table_finale.sort_values(by=x_labels[nom_variable_x], ascending=True, inplace=True)

        fig = px.bar(table_finale, y=y_labels[nom_variable_y], text=y_labels[nom_variable_y], height=550)

        fig.update_traces(textposition='outside')

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
