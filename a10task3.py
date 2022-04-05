# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:03:23 2022

@author: evely
"""

#Evelyn Baranski
#3/29/22
#Efficient Portfolios


#This file is plotting stock prices, cumulative change, and efficient frontier


#Importing required packages
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

#importing from previous task
from a10task2 import *


#Plotting prices
def plot_stock_prices(symbols):
    """This function creates a graph of historical stock
    prices for however many stocks given in string 
    'symbols'."""
    
    #getting df for the stock prices
    prices_df = get_stock_prices_from_csv_files(symbols)
    
    #Gettng x value - Date
    x = prices_df.index
    
    
    #iterating through columns in df, plotting with x
    for col in prices_df.columns:
        
        y = prices_df[col]
        plt.plot(x, y)
    
    
    #altering titles & labels on graph
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Prices')
    
    #adjusting the tiks for x axis
    plt.xticks(x[::2], rotation = 45)
    plt.locator_params(axis='x', nbins=len(x)/15)

    plt.show()


#Plotting cumulative change
def plot_stock_cumulative_change(symbols):
    """This function plots a graph of cumulative stock returns for
    stocks within the list, symbols. Monthly cumulative stock returns."""
    
    stock_df = get_stock_prices_from_csv_files(symbols)

    #getting cumulative changes in price
    cum_change = ((stock_df.iloc[0:] - stock_df.iloc[0]) / stock_df.iloc[0]) + 1
    
    
    #plotting:
    #setting x variable
    x = stock_df.index
    
    #iterating through columns in df, plotting with x
    for col in cum_change.columns:
        
        y = cum_change[col]
        plt.plot(x, y)
    
    
    #altering titles & labels on graph
    plt.xlabel('Date')
    plt.ylabel('Relative Price')
    plt.title('Cumulative Change in Stock Price')
    
    #adjusting the tiks for x axis
    plt.xticks(x[::2], rotation = 45)
    plt.locator_params(axis='x', nbins=len(x)/15)

    plt.show()




#Plotting efficient frontier
def plot_efficient_frontier(symbols):
    """This function creates a graph of the efficient frontier
    (set of min var portfolios) that can be aacheived using
    small set of assets."""
    
    #getting values to calculate range of rate of return
    returns = get_stock_returns_from_csv_files(symbols)
    cov = get_covariance_matrix(returns)

    e = np.matrix(returns.mean())
    v = np.matrix(cov)
    w = calc_global_min_variance_portfolio(v)
    ret = calc_portfolio_return(e, w)

    #creating min and max values for rs
    min_rs = ret - (ret * 5)
    max_rs = ret + (ret * 5)
    
    
    #rates of returns (rs) array
    rs = np.linspace(min_rs, max_rs)
    
    #standard deviation array
    stdev_array = calc_efficient_portfolios_stdev(e, v, rs)
    

    #Plotting stdev vs. list of rates
    plt.plot(stdev_array, rs)
    
    #adding chart titles, etc.
    plt.xlabel('Portfolio Standard Deviation')
    plt.ylabel('Portfolio Expected Return')
    plt.title('Efficient Frontier')
    



if __name__ == '__main__':
    
    symbols = ['AAPL',  'DIS', 'GOOG', 'KO', 'WMT']
    
    #plot_stock_prices(symbols)
    
    plot_stock_cumulative_change(symbols)
    
    #plot_efficient_frontier(symbols)





    
