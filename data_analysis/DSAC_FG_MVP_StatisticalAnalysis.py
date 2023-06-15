import numpy as np
import pandas as pd

from data_collection.classes import Stock

def statsof(data):
  """
  Calculates the minimum, maximum, range, median, mean, variance and
  standard deviation of a given list.

  Parameters
  ----------
  data : list
    List of numerical values to get the statistics from 

  Returns
  -------
  List
    A list with the statistical values calculated form the given data. 
  """

  column = []
  column.extend([min(data), max(data), np.ptp(data), np.median(data),
                np.mean(data), np.var(data), np.std(data)])
  return column



def get_statistics(stock):
  """
  Calculates the minimum, maximum, range, median, mean, variance and
  standard deviation of multiple of a stock object history columns.

  Parameters
  ----------
  stock : stock object
    the stock object with the price history. 

  Returns
  -------
  Pandas Dataframe
    A dataframe with the statistical values calculated form the given data. 
  """

  stats_df = pd.DataFrame(columns=["Open", "High", "Low", "Close", "Volume"],
                          index= ["Min", "Max", "Range", "Median", "Mean", "Variance", "Std" ])

  stats_df["Open"] = statsof(stock.history["Open"])
  stats_df["High"] = statsof(stock.history["High"])
  stats_df["Low"] = statsof(stock.history["Low"])
  stats_df["Close"] = statsof(stock.history["Close"])
  stats_df["Volume"] = statsof(stock.history["Volume"])

  return stats_df