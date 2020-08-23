# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 09:15:29 2020

@author: artur
"""


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor


plt.style.use("classic")


fig, ax = plt.subplots()

x=np.arange(-10,10,0.01) # Määramispiirkond

y1=x
plt.plot(x,y1,linewidth=3) # Esimene funktsioon

y2=4*x-15
plt.plot(x,y2,linewidth=3) # Teine funktsioon

y3=-4*x+30
plt.plot(x,y3,linewidth=3) # Kolmas funktsioon

plt.grid(True)
plt.xlabel("x-telg")
plt.ylabel("y-telg")
plt.plot(0,0, marker="o", color="red", markersize=7)
plt.annotate("(0;0)",(0,0))

cursor=Cursor(ax,horizOn=True,vertOn=True, color="red", linewidth=2)

plt.show()
