import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_market_facts.csv"))
df_long_term_n = pd.read_csv(DATA_PATH.joinpath("df_long_term_business_number.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Dashboard Summary"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    Description of the objective of the dashboard.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Market Facts"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_fund_facts)),
                                ],
                                className="six columns", style={"padding-right":"20px"}
                            ),
                            html.Div(
                                [
                                    
                                    html.H6(
                                        "Number of Authorized Insurers by Class of Insurance Business",
                                        className="subtitle padded",
                                    ),
                                    dcc.Dropdown(['Long Term Business','General Business'] ,'Long Term Business', id='insurer-type-dropdown'),
                                    html.Div(html.Table(id='insurer-type',), style={'height': '200px', 'overflowY': 'auto'},),
                                   
                                    
                                ],
                                className="six columns", 
                                
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.H6(
                                        ["Expert Opinion on the Market"], className="subtitle padded"
                                    ),
                            html.P(
                                        ["Some text from Arthur"]
                            )
                        ]
        
                    )
                ],    
                className="sub_page",
            ),
        ],
        className="page",
    )
