# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 07:55:34 2020

@author: artur
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("default")

fig, ax = plt.subplots()
# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))
# Hide the top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.plot(1,0,">k",transform=ax.get_yaxis_transform(),clip_on=False)
ax.plot(0,1,"^k",transform=ax.get_xaxis_transform(),clip_on=False) # noolte juures saad värvi muuta, nt ">k" annaks musta värvi noole


# Siin saab jaotiste väärtusi muuta omal soovil. np.arange(algus, lõpp, samm)
ax.set_xticks(np.arange(-10, 10 , 1))
ax.set_yticks(np.arange(-10 ,10 , 1))
ax.set_ylim(-6,6)
ax.set_xlim(-6,6)
ax.grid(True)
ax.set_title("y=ax+b graafik", fontsize=18)

# FUNKTSIOONE/PUNKTE JA MUID ASJU SAAD MUUTA SIIN.

def linfunk(x):
    return -3*x+2 # See on meie funktsioon y=ax+b

x=np.linspace(-10,10,50) # Määramispiirkond 
y=linfunk(x) 
ax.plot(x,y, lw=2) # Joonestame joone

x_punktid=[-1, 1] # See on justkui meie tabelis x-ide rida.
for i in x_punktid:
    ax.plot(i, linfunk(i), "ro") # Märgime graafikule punktid
