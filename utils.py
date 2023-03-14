import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.A(
                        html.Img(
                            src=app.get_asset_url("sia-logo.png"),
                            className="logo",
                        ),
                        href="https://www.sia-partners.com/en",
                    ),
                    html.A(
                        html.Button(
                            "Source Data",
                            id="learn-more-button",
                            style={"margin-left": "-10px"},
                        ),
                        href="https://www.ia.org.hk/en/infocenter/statistics/market.html",
                    ),

                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Hong Kong Insurance Authority Dashboard")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/insurance-authority-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/insurance-authority-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "General Business",
                href="/insurance-authority-report/general-business",
                className="tab",
            ),
            dcc.Link(
                "Long Term Business",
                href="/insurance-authority-report/long-term-business",
                className="tab",
            ),
            dcc.Link(
                "About", href="https://www.sia-partners.com/en/about-us/who-we-are", className="tab", target="_blank"
            ),

        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    html_column = []
    for name in df.columns:
        html_column.append(html.Th(name))
    table.append(html.Tr(html_column))
    for index, row in df.iterrows():
  
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


