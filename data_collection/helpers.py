import yfinance as yf
import matplotlib.pyplot as plt
from data_collection.classes import Stock

def get_stock_history(symbol, start="2022-12-31" , end="2023-04-01"):
    """
    Gets the stock history of the specified stock from Yahoo Finance.
    
    Parameters
    ----------
    symbol: str
        The ticker symbol used to represent the stock.
    start : str, optional
        A datetime string that selects the date from which to start
        retrieving stock price data (format: YYYY-MM-DD)
       (Default is "2022-12-31").
    end : str, optional
        A datetime string that selects the date from which to stop
        retrieving stock price data (format: YYYY-MM-DD)
       (Default is "2023-04-01").

    Returns
    -------
    Stock object
        An object containing the stock price history, symbol,
        currency, and timezone
    """
  ticker = yf.Ticker(symbol)
  history = ticker.history(start=start, end=end, interval="1d", repair=True)
  symbol = ticker.history_metadata["symbol"]
  currency = ticker.history_metadata["currency"]
  timezone = ticker.history_metadata["timezone"]

  stock = Stock(symbol, currency, timezone, history)
  return stock