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
shape = (120, 120)

#numpy.zeros(shape, dtype=float, order = 'C', *, like = None)
#Return a new array of given shape type, filled with zeros
img = np.zeros(shape, dtype=np.uint8)

#
raio, centro = disk((55, 55), 60, shape = shape)
img[raio, centro]=1


#Stack arrays in sequence vertically
rock_matrix = np.hstack((np.vstack((img,img)), np.vstack((img,img))))

'''
Extract Coordinates
'''


p = []

for i in range(len(rock_matrix)):
    for j in range(len(rock_matrix[0])):
        if rock_matrix[i,j] ==1:
            p.append([j, len(rock_matrix)-i])

p = np.array(p)

file = open("obst-wall.d90", "w")
np.savetxt(file, p, fmt='%i')


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
