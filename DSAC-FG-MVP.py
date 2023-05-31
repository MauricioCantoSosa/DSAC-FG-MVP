import yfinance as yf
import matplotlib.pyplot as plt
from tabulate import tabulate

from data_collection.classes import Stock
from data_collection.helpers import get_stock_history

if __name__ == "__main__":
    tsla_stock = get_stock_history("TSLA")
    aapl_stock = get_stock_history("AAPL")

    # printing the stocks in a tabular format in the terminal.
    print("\n\n\nTESLA stock\n")
    print(tabulate(tsla_stock.history, headers='keys', tablefmt='fancy_grid'))
    print("\n\n\nAPPLE stock\n")
    print(tabulate(aapl_stock.history, headers='keys', tablefmt='fancy_grid'))

    # Plotting the stock history in a line plot
    tsla_stock.plot_price()
    aapl_stock.plot_price()
