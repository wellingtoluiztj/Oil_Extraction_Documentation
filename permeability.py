#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 01:43:45 2022

@author: wsantos
"""
import pandas as pd
import numpy as np

L = 0.000000174 #float(input('Lenght: '))
mu = 0.597#float(input('Dynamic Viscosity: '))
#====Convertion Factor====
d_X = 0.000000617 #float(input("d_X: "))
d_M = 0.000000000000000213 #float(input("d_M: "))
d_T = 0.0000000308 #float(input("d_T: "))

out_put = pd.read_table('/home/wsantos/Documentos/Doutorado/Projeto_de_Doutorado/Resultados/\
Exemplos_Taxila/meu_modelo_2D/SandStone/\
0.00/Permeability/gnu_output/RES-001.dat',sep='\s+', skiprows=1).values

colx = out_put[:,0]#Select only the column 0 for every rows
col0_lx = colx.tolist()#Turn the array col0 into a list

colv =  out_put[:,4]#Select only the column 4 for every rows
col0_lv = colv.tolist()#Turn the array col0 into a list

colp =  out_put[:,6]#Select only the column 4 for every rows
col0_lp = colp.tolist()#Turn the array col0 into a list


v = []
p = []
pf = []
a= 0
b=0
for n,i in enumerate(col0_lx):
    if i ==1:
        a +=1
        v.append(col0_lv[n])
        p.append(col0_lp[n])
    elif i==319:
        b +=1
        pf.append(col0_lp[n])

p_total = round(sum(p), 4)    
v_total = round(sum(v), 4) #Times 20 to convert
pf_total = round(sum(pf),4)

p_total = (p_total)*(d_M/((d_T)**2)*d_X)
v_total = (v_total)*(d_X/d_T)
pf_total =(pf_total)*(d_M/((d_T)**2)*d_X)


perm = L*mu*((v_total)/(p_total-pf_total))

perm

#*((d_M/((d_T)**2)*d_X)
#*(d_X/d_T)