import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_L8 = pd.read_csv("C:\\Users\\GazizZHUMASH\\Desktop\\IA_Dashboard\\insurance_authority_report\\data\\df_L8.csv")


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
        
                # Row 1

                html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Individual Insurers' Statistics: Non-Linked Individual Life In-Force Business", className="subtitle padded"),
                                    html.Table(make_dash_table(df_L8))
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    
                       
                 ],
                className="sub_page",
            ),
        ],
        className="page",
    )
