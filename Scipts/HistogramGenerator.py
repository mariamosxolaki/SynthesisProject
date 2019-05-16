# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:28:32 2019

@author: Konrad Jarocki
"""

# This scipt is producting numpy array that will be used to make the raster in the other one.
import psycopg2
import numpy as np
import matplotlib.pyplot as plt
#Connect to postgresql database with postGIS extension installed
conn = psycopg2.connect("dbname=histogram user = postgres")
cur = conn.cursor()
#table_name = 'point_cloud1'
#cur.execute("select min(x) as x_min, min(y) as y_min, max(x) as x_max, max(y) as y_max from {};".format(table_name)) 
#Bounding box of the point cloud, required to estimate the size of the grid
x_min = -61874.023437500
y_min = -26957.539062500
x_max = -60830.167968750
y_max = -26137.185546880

#Define the grid
grid_width = abs(x_max-x_min)
grid_height = abs(y_max-y_min)
cell_size = 20
cell_width = int(round(grid_width / cell_size,0) +1)
cell_height = int(round(grid_height / cell_size,0) +1)
print(cell_width,cell_height)
histogram = [[0 for x in range(cell_width)] for y in range(cell_height)] 
#Iterating every cell in the grid
for i in range(cell_width): 
    for j in range(cell_height): 
        #making boundaries for specific cell
        gx_min = x_min + cell_size*i
        gy_min = y_min + cell_size*j
        gx_max = x_min + cell_size*(i+1)
        gy_max = y_min + cell_size*(j+1)
        #query
        cur.execute("SELECT count(*) FROM point_cloud1 where x>={} and x<{} and y>={} and y<{};".format(gx_min,gx_max, gy_min, gy_max)) 
        for record in cur:
            print(i,j,record[0])
            #save the result to array
            histogram[j][i] = record[0]
           
#plot of the results
print(histogram)
f = np.array(histogram)        
plt.imshow(f, interpolation="nearest", origin="upper")
plt.colorbar()
plt.show()