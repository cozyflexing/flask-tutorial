from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)


def create_dash(flask_app):
    dash_app = Dash(
        server=flask_app,
        name="Dashboard",
        url_base_pathname="/dashboard/",
    )

    dash_app.layout = html.Div(
        children=[
            html.H1(children="Hello Dash"),
            html.Div(
                children="""
        Dash: A web application framework for your data.
    """
            ),
            dcc.Graph(
                id="example-graph",
                figure=px.bar(df, x="Fruit", y="Amount", color="City", barmode="group"),
            ),
        ]
    )

    return dash_app
