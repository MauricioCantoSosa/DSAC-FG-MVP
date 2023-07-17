import pandas as pd
import prophet
import matplotlib.pyplot as plt

from data_collection.classes import Stock

def forecast(data, days=365):
    data = pd.DataFrame(data["Close"])
    data.reset_index(inplace=True)
    data.rename(columns={'index': 'ds', 'Close': 'y' }, inplace=True)

    prophetobj = prophet.Prophet(daily_seasonality=True)
    prophetobj.fit(data)
    future_dates = prophetobj.make_future_dataframe(periods=days)
    predictions = prophetobj.predict(future_dates)
    predictionplot = prophet.plot.plot_plotly(prophetobj, predictions)
    return predictionplot