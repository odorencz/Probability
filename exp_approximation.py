# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:27:48 2016

@author: Olivia
"""

import numpy as np #random simulator

rlist = list() #stores rhett values
blist = list() #stores baldwin values
i = 0
while(i<10000): #repeats to get close to real value
    rlist.append(np.random.exponential(2)) #exponential with lambda 1/2
    blist.append(np.random.exponential(3)) #exponential with lambda 1/3
    i = i+1
    
total = 0
for i in range(0,10000):
    if rlist[i]>blist[i]: #adds to the list if r is greater than b 
        total = total +1 
        
print(total/10000) #percent of total where r was greater than b
