"""
Small script to apply the given threshold and plot the results
@author: Konrad Jarocki
"""

import numpy as np
import matplotlib.pyplot as plt

def threshold(fn,th_value):
    #loading histogram from given file
    histogram = np.loadtxt(fn)  
    #iterating every cell
    for index, x in np.ndenumerate(histogram):
        #checking condition
        if x>th_value:
            histogram[index[0],index[1]] = 1
        else:
            histogram[index[0],index[1]] = 0
        #plot of the results
        plt.imshow(histogram, interpolation="nearest", origin="upper")
        plt.colorbar()
        plt.show()
    return histogram