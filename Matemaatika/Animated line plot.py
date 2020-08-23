# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 08:59:28 2020

@author: artur
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# SEE EI TÖÖTA!!!!!!! Punktidega teeb okeilt, joontega töötab valesti. LISA: kuna ax.clear() on peidus, siis joonistab ta eelmise graafiku üle. VÄGA KOORMAV.

tulemused=[]

fig,ax=plt.subplots()

x=np.arange(-10,10,0.1)
y=x**2+3*x-15

x_values=[]
y_values=[]

plt.xlim(-100,100)
plt.ylim(-100,100)


def animate(frame):

    punkt=[x[frame],y[frame]]
    tulemused.append(tuple(punkt))
    
    for punkti_koordinaadid in tulemused:
        x_values.append(punkti_koordinaadid[0])
        y_values.append(punkti_koordinaadid[1])
    # ax.clear()
    ax.grid(True, linestyle="-.")
    ax.plot(x_values,y_values,"ok",markersize=1)
 
ani =FuncAnimation(plt.gcf(), animate, interval= 10)

plt.tight_layout()
plt.show()

