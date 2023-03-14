# # -*- coding: utf-8 -*-

from dash import Dash, dcc, html, Input, Output

import dash
import plotly.graph_objs as go
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
from utils import Header, make_dash_table
from pages import (
    generalBusiness,
    overview,
    longTermBusiness,
)

import pandas as pd
import pathlib

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_g15_a = pd.read_csv("C:\\Users\\GazizZHUMASH\\Desktop\\IA_Dashboard\\insurance_authority_report\\data\\df_g15_a.csv")
df_g15_b = pd.read_csv("C:\\Users\\GazizZHUMASH\\Desktop\\IA_Dashboard\\insurance_authority_report\\data\\df_g15_b.csv")
df_g15_c = pd.read_csv("C:\\Users\\GazizZHUMASH\\Desktop\\IA_Dashboard\\insurance_authority_report\\data\\df_g15_c.csv")
df_L8 = pd.read_csv("C:\\Users\\GazizZHUMASH\\Desktop\\IA_Dashboard\\insurance_authority_report\\data\\df_L8.csv")

df_fund_facts = pd.read_csv("C:\\Users\\GazizZHUMASH\\Desktop\\IA_Dashboard\\insurance_authority_report\\data\\df_market_facts.csv")
df_general_business_n = pd.read_csv("C:\\Users\\GazizZHUMASH\\Desktop\\IA_Dashboard\\insurance_authority_report\\data\\df_general_business_number.csv")
df_long_term_n = pd.read_csv("C:\\Users\\GazizZHUMASH\\Desktop\\IA_Dashboard\\insurance_authority_report\\data\\df_long_term_business_number.csv")

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "Insurance Report"
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content"),html.Div(id="insurer-type"), dcc.Dropdown(id="insurer-type-dropdown"), html.Div(id="direct-business"), dcc.Dropdown(id="direct-business-dropdown"),
     html.Div(id="reinsurance-business"),dcc.Dropdown(id="reinsurance-business-dropdown"), dcc.Graph(id="graph-4"),dcc.Dropdown(id="class-business-dropdown")]
)



# Update page
@app.callback(Output('insurer-type', 'children'), Input('insurer-type-dropdown', 'value'))
def update_output(value):
    if value == 'Long Term Business':
        return  make_dash_table(df_long_term_n)
    elif value == 'General Business':
        return  make_dash_table(df_general_business_n)
    return dash.no_update


# Update page
@app.callback(Output('direct-business', 'children'), Input('direct-business-dropdown', 'value'))
def update_table_p2b(value):
    return  make_dash_table(df_g15_b[df_g15_b['Class of Business']==str(value)])

# Update page
@app.callback(Output('reinsurance-business', 'children'), Input('reinsurance-business-dropdown', 'value'))
def update_table_p2c(value):
    return  make_dash_table(df_g15_c[df_g15_c['Class of Business']==str(value)])


# Update page
@app.callback(Output('graph-4', 'figure'), Input('class-business-dropdown', 'value'))
def update_business_class(value):
    figure={
            "data": [
        
                    go.Scatter(
                            x=df_g15_a[df_g15_a['Class of Business']==str(value)]["Year"],
                            y=df_g15_a[df_g15_a['Class of Business']==str(value)]['Earned Premiums EP $m'],
                            line={"color": "#97151c"},
                            mode="lines",
                            name="Earned Premiums EP $m",
                            ),
                    go.Scatter(
                            x=df_g15_a[df_g15_a['Class of Business']==str(value)]["Year"],
                            y=df_g15_a[df_g15_a['Class of Business']==str(value)]['Net Commissions Payable/(Receivable) $m'],
                            line={"color": "#b5b5b5"},
                            mode="lines",
                            name="Net Commissions Payable/(Receivable) $m",
                            ),
                    go.Scatter(
                            x=df_g15_a[df_g15_a['Class of Business']==str(value)]["Year"],
                            y=df_g15_a[df_g15_a['Class of Business']==str(value)]['Management Expenses $m'],
                            line={"color": "#b5b5b5"},
                            mode="lines",
                            name="Management Expenses $m",
                            ),
                    go.Scatter(
                            x=df_g15_a[df_g15_a['Class of Business']==str(value)]["Year"],
                            y=df_g15_a[df_g15_a['Class of Business']==str(value)]['Unexpired Risks Adjustment $m'],
                            line={"color": "#b5b5b5"},
                            mode="lines",
                            name="Unexpired Risks Adjustment $m",
                            ),
                    go.Scatter(
                            x=df_g15_a[df_g15_a['Class of Business']==str(value)]["Year"],
                            y=df_g15_a[df_g15_a['Class of Business']==str(value)]['Net Claims Incurred $m'],
                            line={"color": "#b5b5b5"},
                            mode="lines",
                            name="Net Claims Incurred $m",
                            ),
                    go.Scatter(
                            x=df_g15_a[df_g15_a['Class of Business']==str(value)]["Year"],
                            y=df_g15_a[df_g15_a['Class of Business']==str(value)]['Underwriting Profit/(Loss) $m'],
                            line={"color": "#b5b5b5"},
                            mode="lines",
                            name="Underwriting Profit/(Loss) $m",
                            ),
                    ],
                    "layout": go.Layout(
                            autosize=True,
                            width=700,
                            height=200,
                            font={"family": "Raleway", "size": 10},
                            margin={
                                    "r": 30,
                                    "t": 30,
                                    "b": 30,
                                    "l": 30,
                                    },
                            showlegend=True,
                            titlefont={
                                "family": "Raleway",
                                "size": 10,
                            },
                            xaxis={
                                                    "autorange": True,
                                                    "range": [
                                                        "2017-01-01",
                                                        "2021-01-01",
                                                    ],
                                                    "rangeselector": {
                                                        "buttons": [
                                                            {
                                                                "count": 1,
                                                                "label": "1Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 3,
                                                                "label": "3Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 4,
                                                                "label": "4Y",
                                                                "step": "year",
                                                            },
                                                            {
                                                                "label": "All",
                                                                "step": "all",
                                                            },
                                                        ]
                                                    },
                                                    "showline": True,
                                                    "type": "date",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [
                                                        18.6880162434,
                                                        278.431996757,
                                                    ],
                                                    "showline": True,
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                     },
    return figure[0]


# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/insurance-authority-report/general-business":
        return generalBusiness.create_layout(app)
    elif pathname == "/insurance-authority-report/long-term-business":
        return longTermBusiness.create_layout(app)
    elif pathname == "/insurance-authority-report/full-view":
        return (
            overview.create_layout(app),
            generalBusiness.create_layout(app),
            longTermBusiness.create_layout(app),
        )
    else:
        return overview.create_layout(app)




if __name__ == "__main__":
    app.run_server(debug=True)
