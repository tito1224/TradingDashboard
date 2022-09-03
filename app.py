from matplotlib.pyplot import figure
from dash import Dash, dcc, html, Input, Output, callback
from numpy import intp
import plotly.express as px
import pandas as pd 
from pages import page1,page2
import dashObjects.dashObjects as do
import requests
import pandas_datareader as pdr

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)