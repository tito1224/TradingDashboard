from dash import dcc, html, Input, Output, callback
import plotly.express as px
import dashObjects.dashObjects as do


# load initial data
dfMarketData = do.getMarketDataEOD(['^GSPC'],'2021-01-01','2021-01-14')
dfMarketData = dfMarketData[['Adj Close','Volume']]
fig1 = px.scatter(x=dfMarketData.index, y = dfMarketData['Adj Close'].values)


layout = html.Div([
    html.H1('Budgeting Dashboard'),

    # select the inputs for use in the graph
    html.Div([
        dcc.Dropdown(["CANADA","USA","LATAM","EUROPE","ASIA","ANZ"],"USA"),
        dcc.Dropdown(options=[
            {'label':'S&P 500', 'value':'^GSPC'},
            {'label':'Russell 2000', 'value':'^RUT'}
        ])
    ],style = {'width':'48%','float':'right','display':'inline-block'}),

    html.Div([
    dcc.Graph(
            id='general-market-data',
            figure=fig1
        )
    ]),

    
    dcc.Dropdown(
        {f'Page 1 - {i}': f'{i}' for i in ['New York City', 'Montreal', 'Los Angeles']},
        id='page-1-dropdown'
    ),
    html.Div(id='page-1-display-value'),
    dcc.Link('Go to Page 2', href='/page2')
])

@callback(
    Output('page-1-display-value', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'