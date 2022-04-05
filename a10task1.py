# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:36:10 2022

@author: evely
"""



#Evelyn Baranski
#3/27/22
#Assignment 10: Efficient Portfolios


#This file, a10task1 is performing linear algebra with numpy for
#bond pricing and analytics

#importing necessary packages
import numpy as np
from numpy.linalg import inv


#Function 1
def bond_price(times, cashflows, rate):
    """This function calculates and returns the price of a bond
    given cashflows and discount rate using linear algebra.
    
    Convert all parameters to numpy matrix, return result as float"""
    
    #Getting list of discount factors
    discounts = [1 / (1 + rate )**x for x in range(1, len(times) + 1)]
    
    #Converting to np matrices
    times = np.array(times)
    cashflows = np.array(cashflows)
    discounts = np.array(discounts)
    
    
    price = cashflows * discounts
    price = float(np.sum(price))
    
    return price




#Function 2
def bootstrap(cashflows, prices):
    """This function implements a bootstrap method taking
    parameters cashflows (2D list/ matrix) and prices, columnn matrix
    containing bond prices and finds the prices of the implied 0 
    coupon bonds, i.e discount factors
    
    d = CF^-1 * P"""

    #converting prices and cashflows to np matrices
    prices = np.matrix(prices)
    cashflows = np.matrix(cashflows) 
    
    #returning bootstrap discount values
    ans =  inv(cashflows) * prices.transpose()
    
    return ans



#Function 3
def bond_duration(times, cashflows, rate):
    """This function calcualtes and returns the duration metric for
    a bond using linear algebra.
    
    D = (1/B) * t * c * dT"""
    
    #getting discounts 
    discounts = [1 / (1 + rate )**x for x in range(1, len(times) + 1)]

    #converting paramters to np arrays
    discounts = np.array(discounts)
    cashflows = np.array(cashflows)
    times = np.array(times)
    
    #calculating and summing answer, returning value
    ans = times * cashflows  * discounts * (1 / bond_price(times, cashflows, rate))
    ans = np.sum(ans)

    return ans

        
    




if __name__ == '__main__':
    
    times = [1, 2, 3]
    cashflows = [10, 10, 110]
    rate = .1
    
    print(bond_price(times, cashflows, rate))
    
    rate = .085
    
    print(bond_price(times, cashflows, rate))
    
    CF = [[105,0,0],[6,106,0],[7,7,107]]
    B = [99.5, 101.25, 100.35]
    print("boot")
    print(bootstrap(CF, B))
    
    times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cashflows = [40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 1040.0]

    print(bond_duration(times, cashflows, .035))    
    
    