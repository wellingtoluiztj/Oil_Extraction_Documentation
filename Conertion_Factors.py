#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 10:34:29 2022
Rotine: Calculate the convertion factors for LBM simulation
@author: wsantos
"""

import matplotlib.pyplot as plt

#====D_X====
L = 0.000050            #float(input('Sample Lenght: '))
N = 81                  #int(input('Number of nodes: '))
d_X = L/N

#====D_M====
rho1 = float(input('Brine Density: '))
rho2 = 829              #float(input('Oil Density: '))
d_M = ((rho1+rho2)/2)*(d_X)**(3)

#====D_T====
gamma = float(input('Interfacial Tension: '))
gamma_LBM = 1.0
d_T = sqrt((gamma_LBM/gamma)*d_M)

#====Interfacial Tension Brine====


D = ((-1.721)**2 - 4*1.361*(gamma_LBM + 0.178))
x1 = (-(-1.721) + D**(1/2)) / (2*(1.361))
x2 = (-(-1.721) - D**(1/2)) / (2*(1.361))

#====Relaxation Time Oil====
tau_oil = (3*nu)+0.5
nu_oil = float(input('Oil Viscosity: '))
nu_oil_LBM = (nu_oil)*(d_T/(d_X)**2)


print(f'Os valores das variáveis são tau_b = {tau}, tau_o = {tau_oil}, gk,k={x1} ou gk,k={x2}')

d_V = d_X/d_T #Velocity