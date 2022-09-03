from dash import dcc, html, Input, Output, callback
import requests
import pandas_datareader.data as web

def generate_table(dataframe, max_rows=10):
    """
    Fuction to generate a table. Tr defines a row of cells in a table. The row's cells can then be established using a mix of <td> (data cell) and <th> header cell elements.
    """
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns]) # creating multiple columns for this header ROW
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns # iloc[i] gives you all columns for that row, then use [col] to select the specific data cell 
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

def getMarketDataEOD(lstTicker,strStartTime,strEndTime):
    """
    Get daily stock prices, volume, historical corporate actions (ie dividends/stock splits) and historical dividends from Yahoo Finance.
    """
    data = web.DataReader(lstTicker, 'yahoo', start = strStartTime, end = strEndTime)
    return data