# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np #random number generator

rlist = list() #R=r
blist=list() #B=b
i = 0
while(i<100000):
   rlist.append(np.random.exponential(2)) #simulates random variable
   blist.append(np.random.exponential(3)) #simulates random variable
   i = i+1 #loop

total = 0
for i in range(0,100000): #loop
    if rlist[i]>blist[i]: #if r>b added to total
        total = total + 1

print(total/100000) #percent of total where r>b