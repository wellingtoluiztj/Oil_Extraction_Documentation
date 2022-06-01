#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:15:19 2022

@author: wsantos
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:10:34 2022

@author: wellington
"""

import numpy as np
from skimage.draw import disk
import matplotlib.pyplot as plt
import random
'''
Draw 2D geometries spaced
'''

#Resolution(matrix dimension)
r = 150
shape = ((2*r)+10, (2*r)+10)

#numpy.zeros(shape, dtype=float, order = 'C', *, like = None)
#Return a new array of given shape type, filled with zeros
img1 = np.zeros(shape, dtype=np.uint8)
img2 = np.zeros(shape, dtype=np.uint8)

R = 130
raio, centro = disk((r,r), r, shape = shape)
raio2, centro2 = disk((R,R), R, shape = shape)


img1[raio, centro]=1
img2[raio2, centro2]=1

#Stack arrays in sequence vertically
rock_matrix = np.hstack((np.vstack((img2,img1,img2)), np.vstack((img1,img1, img2)), np.vstack((img1,img1,img2))))



'''
Extract Coordinates
'''


p = []

for i in range(len(rock_matrix)):
    for j in range(len(rock_matrix[0])):
        if rock_matrix[i,j] ==1:
            p.append([j, len(rock_matrix)-i])

p = np.array(p)

x_inlet = 20 
file = open("obst-wall.d90", "w")
np.savetxt(file, p + x_inlet, fmt='%i')


'''
Porosity Calculation
'''

pts = np.argwhere(rock_matrix==1)


soma_rock = np.sum(rock_matrix==1)
soma_vac = np.sum(rock_matrix==0)
forma = np.shape(rock_matrix)


#sea.heatmap(rock_matrix==1)

#soma_zeros

porosity = soma_vac/(soma_vac + soma_rock)
print(porosity)



plt.imshow(rock_matrix)
