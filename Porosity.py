#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:07:31 2021
@author: wsantos
This file.py extract the digital points from an image to use as a rock model
fluid dynamics simulation. 
In the end we need to have the same porosity
"""
#====packages====
import cv2
import numpy as np
import time
from tqdm import tqdm
import os
import pandas as pd


#====extract cordinates from image====
img = cv2.imread('251_2D2.jpg', 2)
  
p = []

for i in tqdm(range(len(img))):
    for j in range(len(img[0])):
        if img[i,j] >= 180:
            p.append([j, len(img)-i])
p = np.array(p)

file = open("obst-wall.d90", "w")
np.savetxt(file, p, fmt='%i')

#====write all files path inside folder gnu_output in a txt file==== 
path = '/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/Exemplos_Taxila/meu_modelo_2D/SandStone/gnu_output'

lista_nomes = []
for root, dirs, files in os.walk(os.path.abspath(path)):
    for file in files:
        nomes = os.path.join(root, file)
        lista_nomes.append(nomes)
lista_nomes.sort()
files = np.array(lista_nomes) 
arquivos = open('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/Exemplos_Taxila/meu_modelo_2D/SandStone/gnu_output/arquivos.txt', 'w')
np.savetxt(arquivos,files,fmt='%s')

#====Porosity Calculation for NX and NY====
directory = '/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/Exemplos_Taxila/meu_modelo_2D/SandStone/file'
data = directory
file = 'obst-wall.d90'
data = data.replace('file',file, 1)
pontos = len(pd.read_table(data, delim_whitespace=True, skiprows=0, header=None))
NX = 300
NY = 200
por = ((NX*NY)-pontos)/(NX*NY)
por = str(por)

