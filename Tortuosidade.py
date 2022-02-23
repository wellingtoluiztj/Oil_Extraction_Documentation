#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 01:11:35 2021
Calculate Tortuosity by Time-Step
@author: ARAUJO, Wellington
"""
#====Packages====
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#====Tortuosity Calculation====
files = pd.read_table('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/Exemplos_Taxila/meu_modelo_2D/Teste/gnu_output/arquivos.txt',header=None).values.reshape(-1,).tolist()

frame_t = []
t_t = []
data = 'RES-0frame.dat' 

for frame in range(1,101):
    frame_t.append(frame)
    data_inp = pd.read_table(files[frame], sep='\s+', skiprows=1, header=None)
    t = ((((data_inp.iloc[:,4])**2 + (data_inp.iloc[:,5])**2)**(1/2)).sum())/((
    data_inp.iloc[:,4]).sum())
    t_t.append(t)
    print(frame,t)
    
#====Steady state value of tortuosity for this pourosity====
tor = t_t[len(t_t)-1]
tor = str(tor)
#====Time-step====
time_step = []
for i in range(1,5000,50):
    time_step.append(i)


#====Graphy of Tortuosity by time-step====
fig, ax = plt.subplots()  
ax.set_ylabel('Tortuosity') #x-label to the axes.
ax.set_xlabel('Time-Step') # y-label to the axes.
#ax.set_title("Tortuosity change")  # Add a title to the axes.
plt.plot(time_step,t_t,'g',label="scale 1") #Plot to tortuosity by time-step
plt.legend(loc="upper right")
plt.xlim([0, 5000])
plt.ylim([1.42,1.5])
plt.text(2500, 1.45, tor)
plt.show() 



