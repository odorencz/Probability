# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:54:42 2016

@author: Olivia
"""
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat


n = 5000
k = 2000

t = np.linspace(-10, 10, k)

mu0 = 0
sigma0 = 1

mu1 = 2
sigma1 = 1

h0 = np.random.normal(mu0, sigma0, n)
h1 = np.random.normal(mu1, sigma1, n)



FA = list()
MD = list()
FAC = list()
MDC = list()
FAD = list()
MDD = list()
FAE = list()
MDE = list()
FAF = list()
MDF = list()

for i in range(0, k):
    sumh0 = 0
    sumh1 = 0
    abslist = list()
    abslist1 = list()
    for j in range(0, n):
        if h0[j]>t[i]: #part B
            sumh0 = sumh0 + 1
        if h1[j]<t[i]: #part B
            sumh1 = sumh1 + 1
        if abs(h0[j])>t[i]: #part F
            abslist.append(h0[j])
        if abs(h1[j])<t[i]: #part F
            abslist1.append(h1[j])
            
    FA.append(sumh1/n) #part B
    MD.append(sumh0/n) #part B
    FAF.append(len(abslist)/n) #part F
    MDF.append(len(abslist1)/n) #part F

minlisth0 = list()
minlisth1 = list()
medlisth0 = list()
medlisth1 = list()
meanlisth0 = list()
meanlisth1 = list()
for i in range(0,k):   
    h2 = np.random.normal(mu0, sigma0, 3)
    h3 = np.random.normal(mu1, sigma1, 3)
    minlisth0.append(min(h2)) #part C
    minlisth1.append(min(h3)) #part C
    medlisth0.append(stat.median(h2)) #part D
    medlisth1.append(stat.median(h3)) #part D
    meanlisth0.append(sum(h2)/3) #part E
    meanlisth1.append(sum(h3)/3) #part E
    

print(t)

for i in range(0, k):
     minhigh = list()
     minhighh1 = list()
     medhigh = list()
     medhigh1 = list()
     meanhigh = list()
     meanhigh1 = list()
     for j in range(0, k):
        if minlisth0[j]>t[i]: #part C
            minhigh.append(minlisth0[j])
        if minlisth1[j]<t[i]: #part C
           minhighh1.append(minlisth1[j])
        if medlisth0[j]>t[i]: #part D
            medhigh.append(medlisth0[j])
        if medlisth1[j]<t[i]: #part D
            medhigh1.append(medlisth1[j])
        if meanlisth0[j]>t[i]: #part E
            meanhigh.append(meanlisth0[j])
        if meanlisth1[j]<t[i]: #part E
            meanhigh1.append(meanlisth1[j])
            
            
     FAC.append(len(minhigh)/k)
     MDC.append(len(minhighh1)/k)
     FAD.append(len(medhigh)/k)
     MDD.append(len(medhigh1)/k)
     FAE.append(len(meanhigh)/k)
     MDE.append(len(meanhigh1)/k)


plt.plot(FA, MD) #part b
plt.plot(FAC,MDC) #Part c
plt.plot(FAD, MDD) #part d
plt.plot(FAE, MDE) #part e
plt.plot(FAF,MDF) #part f
plt.show()
