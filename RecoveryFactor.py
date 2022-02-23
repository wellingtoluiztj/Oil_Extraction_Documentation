#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 01:11:35 2021
Calculate Tortuosity by Time-Step
@author: ARAUJO, Wellington
"""
#Steps:
    #Read table containing density fluids values.
    #Sum of density fluid 1(brine outer - column 3)
    #Sum of density fluid 2(oil inner - column 4)
    #Calculate percentage of density oil there is over time time 

#====Packages====
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import os
#====Convertion Factor====
d_T = 0.012324 #float(input('d_T: '))

'''
Here, we are going to work with 0.00 NaCl
'''

#====Create Arquivos.txt====
path = '/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/0.00/gnu_output/'
list_files = []
for root, dirs, files in os.walk(os.path.abspath(path)):
    for file in files:
        file_name = os.path.join(root, file)
        list_files.append(file_name)
list_files.sort()
array_files = np.array(list_files)
print (array_files)
arquivos = open('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/\
Resultados/Exemplos_Taxila/meu_modelo_2D/SandStone/0.00/gnu_output/arquivos.txt', 'w')
np.savetxt(arquivos,array_files,fmt='%s')

#====Reading density columns====

files = pd.read_table('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/0.00/\
gnu_output/arquivos.txt',header=None).values.reshape(-1,).tolist()#
den_0 = pd.read_table('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/0.00/gnu_output/RES-000.dat', sep='\s+', skiprows=1).values
int_0 = den_0[:,3].sum()
directory = 'file'
data = directory
frame_t = []
oil_ext0 = []
t = 0
for file in files:
    temp = data.replace('file',file, 1)
    t += 1
    frame_t.append(t*(d_T))
    den_i = pd.read_table(temp, sep='\s+', skiprows=1).values
    int_i = den_i[:,3].sum()
    ext = 100*(1-(int_i/int_0))
    oil_ext0.append(ext)
    print(ext)    
frame_t = np.array(frame_t)
oil_ext0 = np.array(oil_ext0)


'''
Here, we are going to work with NaCl = 0.50 
'''

path = '/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/0.50/gnu_output/'

list_files = []
for root, dirs, files in os.walk(os.path.abspath(path)):
    for file in files:
        file_name = os.path.join(root, file)
        list_files.append(file_name)
list_files.sort()
array_files = np.array(list_files)
print (array_files)
arquivos = open('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/0.50/gnu_output/arquivos.txt', 'w')
np.savetxt(arquivos,array_files,fmt='%s')

#====Extraction Calculation====

files = pd.read_table('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/0.50/\
gnu_output/arquivos.txt',header=None).values.reshape(-1,).tolist()

den_0 = pd.read_table('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/0.50/gnu_output/RES-000.dat', sep='\s+', skiprows=1).values
int_0 = den_0[:,3].sum()


directory = 'file'
data = directory

oil_ext1 = []
t = 0
for file in files:
    temp = data.replace('file',file, 1)
    t += 1
    den_i = pd.read_table(temp, sep='\s+', skiprows=1).values
    int_i = den_i[:,3].sum()
    ext = 100*(1-(int_i/int_0))
    oil_ext1.append(ext)
    print(ext)    
    
'''
Were we are going to work with NaCl = 1.00
'''


path = '/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/1.00/gnu_output/'

list_files = []
for root, dirs, files in os.walk(os.path.abspath(path)):
    for file in files:
        file_name = os.path.join(root, file)
        list_files.append(file_name)
list_files.sort()

array_files = np.array(list_files)
print (array_files)
arquivos = open('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/1.00/gnu_output/arquivos.txt', 'w')
np.savetxt(arquivos,array_files,fmt='%s')

#====Extraction Calculation====

files = pd.read_table('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/1.00/gnu_output/arquivos.txt',header=None).values.reshape(-1,).tolist()

den_0 = pd.read_table('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/1.00/gnu_output/RES-000.dat', sep='\s+', skiprows=1).values
int_0 = den_0[:,3].sum()


directory = 'file'
data = directory

oil_ext2 = []
for file in files:
    temp = data.replace('file',file, 1)
    den_i = pd.read_table(temp, sep='\s+', skiprows=1).values
    int_i = den_i[:,3].sum()
    ext = 100*(1-(int_i/int_0))
    oil_ext2.append(ext)
    print(ext)    

'''
Were we are going to plot the graph
'''
listay = []
listax = []
for i in range(0,100):
    listay.append(i)
    listax.append(0.3)

fig, ax = plt.subplots()  
ax.set_ylabel('Oil Extraction(%)') #x-label to the axes.
ax.set_xlabel('Time-Step(micro-second)') # y-label to the axes.
#ax.set_title("Tortuosity change")  # Add a title to the axes.
plt.plot(frame_t, oil_ext0,'g',label = 'NaCl(0.00)') #Plot to Recovery Factor by time-step
plt.plot(frame_t,oil_ext1,'r', label = 'NaCl(0.50)') 
plt.plot(frame_t,oil_ext2,'b', label = 'NaCl(1.00)') 
plt.plot(listax, listay,'--y', label = 'Breack Through') 
plt.legend(loc="lower right")#upper right, best, center left, ...
#plt.xlim([0, 1.3])
#plt.ylim([0,100])
#plt.text(2500, 1.45, tor)
plt.show() 
   