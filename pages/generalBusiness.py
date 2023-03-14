import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_g15_a = pd.read_csv(DATA_PATH.joinpath("df_g15_a.csv"))
df_g15_b = pd.read_csv(DATA_PATH.joinpath("df_g15_b.csv"))
df_g15_c = pd.read_csv(DATA_PATH.joinpath("df_g15_c.csv"))



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
                                    html.H6("Direct & Reinsurance Inward Business", className="subtitle padded"),
                                    dcc.Dropdown(['Accident & Health','Motor Vehicle','Aircraft','Ships','Goods In Transit','Property Damage','General Liability','Pecuniary Loss','Non- Proportional Treaty','Proportional Treaty','Overall'] ,'Accident & Health', id='class-business-dropdown'),
                                   
                                    html.Div(
                                    dcc.Graph(
                                        id="graph-4",
                                        
                                        config={"displayModeBar": False},
                                    )),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    
                                    html.H6(
                                        "Direct Business",
                                        className="subtitle padded",
                                    ),
                                    dcc.Dropdown(['Accident & Health','Motor Vehicle','Aircraft','Ships- Statutory','Ships- Others','Goods In Transit','Property Damage','General Liability - Statutory','General Liability - Others','Pecuniary Loss','Overall'] ,'Accident & Health', id='direct-business-dropdown'),
                                    html.Div(html.Table(id='direct-business',), style={'height': '310px' ,'overflowY': 'auto'},),
                                #    html.Div(html.Table(make_dash_table(df_g15_b)), style={'height': '200px', 'width': '720px' ,'overflowY': 'auto'},)
                                    
                                ],
                                className="twelve columns", 
                                
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    
                                    html.H6(
                                        "Reinsurance Inward Business",
                                        className="subtitle padded",
                                    ),
                                    dcc.Dropdown(['Accident & Health','Motor Vehicle','Aircraft','Ships','Ships- Others','Goods In Transit','Property Damage','General Liability - Statutory','General Liability','Pecuniary Loss','Non- Proportional Treaty','Proportional Treaty','Overall'] ,'Accident & Health', id='reinsurance-business-dropdown'),
                                    html.Div(html.Table(id='reinsurance-business',), style={'height': '310px' ,'overflowY': 'auto'},),
                                #    html.Div(html.Table(make_dash_table(df_g15_b)), style={'height': '200px', 'width': '720px' ,'overflowY': 'auto'},)
                                    
                                ],
                                className="twelve columns", 
                                
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),

               
                 ],
                className="sub_page",
            ),
        ],
        className="page",
    )
