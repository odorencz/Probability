# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:49:40 2016

@author: Olivia
"""

import numpy as np
from matplotlib import pyplot as plt

q= .1
q2=.9


qlist = list()
qlist2 = list()
nlist = list()

for i in range(1,100):
    individlist = list()
    individlist2 = list()
    nlist.append(i)
    for j in range(1,100):
        individlist.append(np.random.binomial(i, q)/i)
        individlist2.append(np.random.binomial(i, q2)/i)
    qlist2.append(sum(individlist2)/99)
    qlist.append(sum(individlist)/99)



plt.plot(nlist,qlist)
plt.plot(nlist, qlist2)
plt.show()

