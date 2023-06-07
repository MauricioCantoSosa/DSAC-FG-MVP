import json

import yfinance as yf
import matplotlib.pyplot as plt
import boto3
from tabulate import tabulate

from data_collection.classes import Stock
from data_collection.helpers import get_stock_history
from data_storage.DSAC_FG_MVP_Storage import store_stock_history, retrieve_stock_history

if __name__ == "__main__":
    tsla_stock = get_stock_history("TSLA")
    aapl_stock = get_stock_history("AAPL")

    # Reading the configuration file with the key access to an 
    # authorized user for the s3 bucket
    with open("DSAC-FG-MVP-Configuration.JSON", "r") as jsonfile:
        datajson = json.load(jsonfile)
    
    # Initializing a connection with the s3 user
    s3 = boto3.resource(
        service_name = 's3',
        region_name = datajson["AWS_DEFAULT_REGION"],
        aws_access_key_id = datajson["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key = datajson["AWS_SECRET_ACCESS_KEY"]
    )

    # Storing acquired stock information in the s3 bucket
    store_stock_history(s3, tsla_stock)
    store_stock_history(s3, aapl_stock)

    # Retrieving the stock history od the selected stock symbol
    tsla_stock = retrieve_stock_history(s3, "tsla")
    aapl_stock = retrieve_stock_history(s3, "aapl")
    
    # printing the stocks in a tabular format in the terminal.
    print("\n\n\nTESLA stock\n")
    print(tabulate(tsla_stock.history, headers='keys', tablefmt='fancy_grid'))
    print("\n\n\nAPPLE stock\n")
    print(tabulate(aapl_stock.history, headers='keys', tablefmt='fancy_grid'))

    # Plotting the stock history in a line plot
    tsla_stock.plot_price()
    aapl_stock.plot_price()
