import json

import logging
import pandas as pd
from botocore.exceptions import ClientError

from data_collection.classes import Stock

def store_stock_history(s3, stock):
    """
    Converts a Stock object, converts it into JSON and stores it into
    an s3 bucket

    Parameters
    ----------
    s3 : boto3 resource
        The boto3 resource user authorized to write on the bucket
    stock : stock
        Stock class instance with stock history data.

    Returns
    -------
    True if file was uploaded, False if not.
    """

    # Converts Stock object into JSON
    dictstock = vars(stock)
    dictstock["history"] = dictstock["history"].to_json()
    jsonstock = json.dumps(dictstock)

    # Uploads file
    try:
        s3.Bucket("dsac-fg-mvp").put_object(Body = jsonstock, Key = f"{stock.symbol}.JSON")
    except ClientError as e:
        logging.error(e)
        return False
    return True

def retrieve_stock_history(s3, symbol):
    """
    Retrieves JSON stock data from s3 bucket and instantiates it 
    into a stock object

    parameters
    ----------
    s3 : boto3 resource
        The boto3 resource user authorized to write on the bucket
    symbol: str
        The ticker symbol used to represent the stock.
    
    Returns
    -------
    Stock object
        An object containing the stock price history, symbol,
        currency, and timezone
    """

    # Retrieves stock data
    retrieved_stock = s3.Bucket("dsac-fg-mvp").Object(f"{symbol.upper()}.JSON").get()['Body'].read().decode('utf-8')
    retrieved_json = json.loads(retrieved_stock)
    retrieved_json["history"] = pd.read_json(retrieved_json["history"])

    #Instantiates data into a Stock object
    stock = Stock(retrieved_json["symbol"], retrieved_json["currency"], retrieved_json["timezone"], retrieved_json["history"])
    return stock