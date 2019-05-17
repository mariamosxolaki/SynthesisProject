# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:25:58 2019

@author: konra
"""

import numpy as np
import matplotlib.pyplot as plt
print(histogram)
histogram = np.loadtxt('histogram_1m.txt')  
for index, x in np.ndenumerate(histogram):
    if x>700:
        histogram[index[0],index[1]] = 1
    else:
        histogram[index[0],index[1]] = 0
        
plt.imshow(histogram, interpolation="nearest", origin="upper")
plt.colorbar()
plt.show()