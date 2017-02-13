# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:43:48 2016

@author: Olivia
"""

import numpy as np
import matplotlib.pyplot as plt

def statts(k):
    rbaselist = list() #store rhett lightbulb lives
    bbaselist = list() #store baldwin lightbulb lives
    for i in range(0, k): #does k random numbers
        rbaselist.append(np.random.exponential(2)) #k rhett lightbulbs
        bbaselist.append(np.random.exponential(3)) #k baldwin lightbulbs
    rcount = sum(rbaselist) #sum of list is total lifetime
    bcount = sum(bbaselist)
    if rcount>bcount: #if r had longer lifteime, continue to buy r 
        expectedtotal = 3*k + 2*(100-k)
    else: #if b had longer lifetime, continue to buy b
        expectedtotal = 2*k + 3*(100-k)
  
   # print(expectedtotal)
    return(expectedtotal) #return the expected total lifetime

xval = list() #x range for plot

for i in range(0,49):
    xval.append(i) #fills list xval with xvals.

yval = list() 
for i in range(0, 49):
    yval.append(0*i) #empty list so we can add values later
    
for i in xval:
        for j in range(0, 12000): #repeat a bunch of times so we get a bunch of trials
            yval[i] = yval[i] + statts(i+1) #adds the expected total to the running total
        
for i in range(0, 49):
    yval[i] = yval[i]/12000 #finds average
    xval[i] = xval[i] +1 #makes the xvals be correct

#print(max(yval), yval.index(max(yval))) #for testing shows max yval and where that value is
print(yval[0])

plt.plot(xval, yval) #prints plot
plt.show()