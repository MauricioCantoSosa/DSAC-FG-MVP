import matplotlib.pyplot as plt

from data_collection.classes import Stock


def plot_price(stock):
  """
  Displays plot of closing price history

  Parameters
  ----------
  stock : stock object
    the stock object with the price history to visualize it. 
  """

  plt.figure(figsize=(10,10))
  plt.plot(stock.history.index, stock.history['Close'])
  plt.xlabel("Date")
  plt.ylabel(f"Price ({stock.currency})")
  plt.title(f"{stock.symbol} Stock Price 01/01/23 - 31/03/23")
  plt.show()

def plot_sma(stock):
  """
  Displays plot of stock closing price history along with both
  simple and long therm simple moving averages.
  
  Parameters
  ----------
  stock : stock object
    the stock object with the price history to visualize it. 
  short_window : int, optional
    The day window of the short term sma (default is 5)
  long_window : int, optional
    The day window of the long term sma (default is 20)
  """

  # Calculating short and long moving averages
  stock.history["Moving Average Short"] = stock.history['Close'].rolling(window=5).mean()
  stock.history["Moving Average Long"] = stock.history['Close'].rolling(window=20).mean()
  
  plt.figure(figsize=(10,10))
  plt.plot(stock.history["Moving Average Short"], 'g--', label="Moving Average 5d")
  plt.plot(stock.history["Moving Average Long"], 'r--', label="Moving Average 20d")
  plt.plot(stock.history['Close'], label="Close")
  plt.xlabel("Date")
  plt.ylabel(f"Price ({stock.currency})")
  plt.title(f"{stock.symbol} Stock Price with Moving Averages 01/01/23 - 31/03/23")
  plt.legend()
  plt.show()

def plot_bollinger(stock):
  """
  Displays plot of stock closing price history along with
  its bollinger bands.

  Parameters
  ----------
  stock : stock object
    the stock object with the price history to visualize it. 
  """

  # Calculating the Bolliger bands
  stock.history['middle_band'] = stock.history['Close'].rolling(window=20).mean()
  stock.history['upper_band'] = stock.history['Close'].rolling(window=20).mean() + stock.history['Close'].rolling(window=20).std()*2
  stock.history['lower_band'] = stock.history['Close'].rolling(window=20).mean() - stock.history['Close'].rolling(window=20).std()*2

  plt.figure(figsize=(10,10))
  plt.plot(stock.history['upper_band'], 'g--', label="Upper band")
  plt.plot(stock.history['middle_band'], 'r--', label="Middle band")
  plt.plot(stock.history['lower_band'], 'y--', label="Lower band")
  plt.plot(stock.history['Close'], label="Close")
  plt.xlabel("Date")
  plt.ylabel(f"Price ({stock.currency})")
  plt.title(f"{stock.symbol} Stock Price with Bollinger Bands 01/01/23 - 31/03/23")
  plt.legend()
  plt.show()