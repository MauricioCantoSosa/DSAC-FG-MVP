import matplotlib.pyplot as plt

class Stock:
    """
    A class used to represent an individual stock

    ...

    Attributes
    ----------
    symbol : str
        The ticker symbol used to represent the stock.
    currency : str
        The currency at which the stock is traded.
    timezone : str
        The timezone at which the stock market that trades
        the stock is based.
    history : pandas.core.frame.DataFrame
        The price and volume history of the stock.

    Methods
    -------
    plot_price()
        Displays plot of stock closing price history.

    plot_sma()
        Displays plot of stock closing price history along with both
        simple and long therm simple moving averages.

    plot_bollinger()
        Displays plot of stock closing price history along with
        its bollinger bands.
    """

    def __init__(self, symbol, currency, timezone, history):
        """
        Parameters
        ----------
        symbol : str
            The ticker symbol used to represent the stock.
        currency : str
            The currency at which the stock is traded.
        timezone : str
            The timezone at which the stock market that trades
            the stock is based.
        history : pandas.core.frame.DataFrame
            The price and volume history of the stock.
        """

        self.symbol = symbol
        self.currency = currency
        self.timezone = timezone
        self.history = history
    
    def plot_price(self):
        """
        Displays plot of closing price history
        """

        plt.figure(figsize=(10,10))
        plt.plot(self.history.index, self.history['Close'])
        plt.xlabel("Date")
        plt.ylabel(f"Price ({self.currency})")
        plt.title(f"{self.symbol} Stock Price 01/01/23 - 31/03/23")
        plt.show()

    def plot_sma(self):
        """
        Displays plot of stock closing price history along with both
        simple and long therm simple moving averages.

        Parameters
        ----------
        short_window : int, optional
            The day window of the short term sma (default is 5)
        long_window : int, optional
            The day window of the long term sma (default is 20)
        """

        self.history["Moving Average Short"] = self.history['Close'].rolling(window=5).mean()
        self.history["Moving Average Long"] = self.history['Close'].rolling(window=20).mean()

        plt.figure(figsize=(10,10))
        plt.plot(self.history["Moving Average Short"], 'g--', label="Moving Average 5d")
        plt.plot(self.history["Moving Average Long"], 'r--', label="Moving Average 20d")
        plt.plot(self.history['Close'], label="Close")
        plt.xlabel("Date")
        plt.ylabel(f"Price ({self.currency})")
        plt.title(f"{self.symbol} Stock Price with Moving Averages 01/01/23 - 31/03/23")
        plt.legend()
        plt.show()

    def plot_bollinger(self):
        """
        Displays plot of stock closing price history along with
        its bollinger bands.
        """

        self.history['middle_band'] = self.history['Close'].rolling(window=20).mean()
        self.history['upper_band'] = self.history['Close'].rolling(window=20).mean() + self.history['Close'].rolling(window=20).std()*2
        self.history['lower_band'] = self.history['Close'].rolling(window=20).mean() - self.history['Close'].rolling(window=20).std()*2
        
        plt.figure(figsize=(10,10))
        plt.plot(self.history['upper_band'], 'g--', label="Upper band")
        plt.plot(self.history['middle_band'], 'r--', label="Middle band")
        plt.plot(self.history['lower_band'], 'y--', label="Lower band")
        plt.plot(self.history['Close'], label="Close")
        plt.xlabel("Date")
        plt.ylabel(f"Price ({self.currency})")
        plt.title(f"{self.symbol} Stock Price with Bollinger Bands 01/01/23 - 31/03/23")
        plt.legend()
        plt.show()