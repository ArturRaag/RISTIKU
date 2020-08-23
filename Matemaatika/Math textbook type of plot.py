# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 07:55:34 2020

@author: artur
"""


import numpy as np
import matplotlib.pyplot as plt

plt.style.use("classic")

fig, ax = plt.subplots()
# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))
# Hide the top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.plot(1,0,">",transform=ax.get_yaxis_transform(),clip_on=False)
ax.plot(0,1,"^",transform=ax.get_xaxis_transform(),clip_on=False) # noolte juures saad värvi muuta, nt ">k" annaks musta värvi noole

x=np.arange(-100.0,100.0,0.01)
y=x**2+3*x-15

ax.plot(x,y)
plt.grid(True)
plt.plot(0,0,"o",color="red")
plt.show()