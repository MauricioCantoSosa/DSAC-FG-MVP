from dash import Dash, dcc, html, Output, Input, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dash_table
import pandas as pd

from forecasting.DSAC_FG_MVP_Forecasting import forecast

# Structures and initializes Dashboard
def start_dash(stock, stock_stats):
    """
    Structures the graphs for the dashboard and initializes it in local host.
        
    Parameters
    ----------
    stock: Stock class
        Stock class instance with stock history data.
    stock_stats : Pandas Dataframe
        Dataframe which includes the statistics of the stock history
    """
    prediction = forecast(stock.history)

    app = Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])

    app.layout = dbc.Container([
      html.H1('{} Stock Prices'.format(stock.symbol), style={'textAlign': 'center'}),
      
      # Integer input box to filter datapoints with less trading
      # volume than selected
      dbc.Row([
            dbc.Col([html.Label('Trading Volume Over:'),
                  dcc.Input(id='trade-volume', type='number', min=0,
                          max=999999999, step=10000, value=0)
          ], width=4),
      ]),
      
      dbc.Row([
      dbc.Col([html.Label('CandleStick Chart')], width=dict(size=4, offset=2)),
      dbc.Col([html.Label('Closing Price Over Time')], width=dict(size=4, offset=2)),
      ]),
      
      dbc.Row([
            # CandleStick graph
            dbc.Col([dcc.Graph(id='candle', figure={}, style={'height': '45vh', 'margin' : '0px'})], width=6),
            # Time series closing price plot
            dbc.Col([dcc.Graph(style={'height': '45vh', 'margin' : '0px'}, figure=
                               {"data" : [{"x" : stock.history.index, "y" : stock.history.Close, "type" : "line"}]},
                            ), 
                    ], width = 6),
      ]),

      dbc.Row([
      dbc.Col([html.Label('Statistics Table')], width=dict(size=4, offset=2)),
      dbc.Col([html.Label('Trading Volume Over Time')], width=dict(size=4, offset=2))
      ]),

      dbc.Row([
            # Statistics table
            dbc.Col([dash_table.DataTable(id='stats_table',
                                        columns=[{"name": i, "id": i} for i in stock_stats.columns],
                                        data=stock_stats.to_dict("records"))
            ], width = 6, align="center"),
            # Trading Volume bar chart
            dbc.Col([dcc.Graph(style={'height': '45vh', 'margin' : '0px'}, figure=
                               {"data" : [{"x" : stock.history.index, "y" : stock.history.Volume, "type" : "bar"}]}
                               )
                    ]),
        ]),

      html.H1('Prediction', style={'textAlign': 'center'}),

      dbc.Row([
            # Prophet prediction plot
            dbc.Col([dcc.Graph(style={'height': '45vh', 'margin' : '0px'}, figure= prediction)], width = 12),
      ]),
    ], fluid=True)


    @callback(
        Output(component_id='candle', component_property='figure'),
        Input(component_id='trade-volume', component_property='value')
    )


    def build_graphs(chosen_volume):  # represents that which is assigned to the component property of the Input
        dff = stock.history[stock.history.Volume > chosen_volume]
        print(dff.head())

        fig_candle = go.Figure(
            go.Candlestick(x=dff.index,
                        open=dff['Open'],
                        high=dff['High'],
                        low=dff['Low'],
                        close=dff['Close'],
                        text=dff['Volume'])
        )

        fig_candle.update_layout(margin=dict(t=30, b=30)) 
        
        return fig_candle

    app.run_server(debug = True)