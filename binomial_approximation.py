# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:33:06 2016

@author: Olivia
"""

import numpy as np

q= .3333
n = 100

qlist = list()

for i in range(0,10000):
    qlist.append(np.random.binomial(n, q)/n)

qest = sum(qlist)/10000

print(qest)

q2 = .3333
    
q2list = list()

for i in range(0,10000):
    q2list.append(np.random.geometric(q2))

q2est = 1/(sum(q2list)/10000)

print("est 1: ", qest)
print("est 2: ", q2est)
