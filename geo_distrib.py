# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 00:01:34 2016

@author: Olivia
"""

import numpy as np
from matplotlib import pyplot as plt

q = np.linspace(0.001, 1, 1000)

qlist = list()

qmeanlist = list()


for i in range(0,1000):
    indlist = list()
    qerrlist = list()
    for j in range(0,1000):
        indlist.append(np.random.geometric(q[i]))
    mean = sum(indlist)/1000
    qerrlist.append(indlist[i]-mean)
    qmeanlist.append(sum(qerrlist)/1000)
    qlist.append(mean)
    



print(qmeanlist)
    
plt.plot(q, qlist)
plt.ylim([0,10])
plt.scatter(q, qmeanlist)
plt.show()