import pandas as pd
import pickle
import numpy as np
from dash import dcc, html, Dash
from dash.dependencies import Input, Output
from lightgbm import LGBMClassifier


train = pd.read_csv("train.csv")
variables = [x for x in train.columns if x != "price_range"]
dict_variables = [{'value':var, "label": var} for var in variables]
app = Dash()

app.layout = html.Div(
    children = [
        html.H1(
            id = "titulo",
            children = "Dashboard teléfonos moviles"
        ),
        dcc.Tabs(
            id = "tabs",
            children = [
                dcc.Tab(
                    id = "primer-tab",
                    value = "Descriptivo",
                    label = "Descriptivo"
                ),
                dcc.Tab(
                    id = "segundo-tab",
                    value = "Modelo",
                    label = "Modelo"
                )   
            ],
        ),
        html.Div(
        id = "resultado-tabulacion"
        )
    ]
) 

@app.callback(
    [
        Output("resultado-tabulacion", "children"),
        Input("tabs", "value")
    ]
)
def layout_tabulacion(tab):

    if tab == "Descriptivo":
        return [html.Div(
            children = [
                html.H3(
                    id = "titulo-tab-1",
                    children = "Graficas descriptivas"
                ),
                html.Div(
                   id = "descriptivo",
                   children = [
                    dcc.Dropdown(
                        id = 'desplegable',
                        options = dict_variables,
                        placeholder = "Selecciona una variable",
                        value = variables[0]
                    ),
                   ]
               )
            ]
        )]
    elif tab == "Modelo":
        return [html.Div(
            children = [
                html.H3(
                    id = "titulo-tab-2",
                   children = "Analisis del modelo"
               ),
               html.Div(
                   id = "inferencias"
               )
            ]
            )]
    else:
        return [html.Div()]

#@app.callback(
#    [
#        Output('descriptivo','children'),
#        Input('desplegable','value'),
#    ]
#)

if __name__ == '__main__':
    app.run_server(debug=True)