# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:12:05 2016

@author: Olivia
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
from scipy.stats import norm

Wlist = list()
Xlist = list()
Ylist = list()

Wtotal = 0
Xtotal = 0
Ytotal = 0
c = 0;

for i in range(0,10000):
    w = np.random.binomial(6, 1/6) #generates random numbers
    x = np.random.binomial(12,1/6)
    y = np.random.binomial(18,1/6)
    Wlist.append(w) #adds to a list 
    Xlist.append(x)
    Ylist.append(y)
    if w>=1: #if more than one six add to total
        Wtotal += 1
    if x>=2:
        Xtotal += 1
    if y>=3:
        Ytotal += 1
    c += 1;
        
print("P[W]=", Wtotal/10000, " P[X]=", Xtotal/10000, " P[Y]=", Ytotal/10000) #part b

whelp = {0:0,1:0,2:0,3:0,4:0,5:0,6:0} #dictionaries
xhelp = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
yhelp = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0}

for j in range(0,10000):
    for i in range(0,7):
        if(Wlist[j]==i):
            whelp[i] += 1 #counts how many for each number
    for i in range(0,13):
        if(Xlist[j]==i):
            xhelp[i] += 1
    for i in range(0, 19): 
        if(Ylist[j]==i):
            yhelp[i] += 1

xwlist = []
xxlist = []
xylist = []

for i in range(0,7):
    whelp[i] = whelp[i]/10000 #probability
    xwlist.append(i)
for i in range(0, 13):
    xhelp[i] = xhelp[i]/10000
    
for i in range(0,19):
    yhelp[i] = yhelp[i]/10000
  

w=[]
x=[]
y=[]

for i in range(0,6):
    whelp[i+1]=whelp[i]+whelp[i+1] #convert to cdf
for i in range(0, 12):
    xhelp[i+1]=xhelp[i]+xhelp[i+1]
for i in range(0, 18):
    yhelp[i+1]=yhelp[i]+yhelp[i+1]

for i in range(0,7):
    w.append(whelp[i]) #puts in list so it is plottable
for i in range(0,13):
    x.append(xhelp[i])
for i in range(0, 19):
    y.append(yhelp[i])
 
for i in range(0, 6):
    xxlist.append(i) #sets up x values for plot
    xxlist.append(i+.5)
    xylist.append(i)
    xylist.append(i+1/3)
    xylist.append(i+2/3)
xylist.append(6)
xxlist.append(6)

mu1 = 1 #used for normal. expected value
sigma1 = math.sqrt(5/6) #standard deviation
sigma2 = math.sqrt(5/13)/2
sigma3=math.sqrt(2.5)/3

xx = []
xxx=[]
xxxx=[]
xxxxx=[]
for i in range(1,1000):
    xxx.append(norm.cdf(100/i,mu1,sigma1)) #norm.cdf doesn't graph so have to calculate values and use those to graph
    xxxx.append(norm.cdf(100/i,mu1,sigma2))
    xxxxx.append(norm.cdf(100/i,mu1,sigma3))
    xx.append(100/i)
    


plt.plot(xylist,y)
plt.plot(xxlist,x)
plt.plot(xwlist,w) 
#plt.plot(xx,xxx)
#plt.plot(xx,xxxx)
#plt.plot(xx,xxxxx)
plt.xlim(xmax = 3) #sets window
plt.show #show all