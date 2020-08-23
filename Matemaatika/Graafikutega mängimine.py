# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 05:49:31 2020

@author: artur
"""


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor


plt.style.use('classic') # Optional, stiile on erinevaid. Minu lemmikud: classic, dark_background

x=np.arange(-10,11, 0.001)
y=x**2-15

fig,ax=plt.subplots()

p = plt.plot(x,y,"-", linewidth=3)
ax.grid(True)
ax.plot(0,0, marker="o", color="red")
ax.annotate("(0,0)", (0,0))
plt.ylabel("y-telg")
plt.xlabel("x-telg")

cursor = Cursor(ax, horizOn=True,vertOn=True, color='gold', linewidth=1) # Huvitav cursor. Ilma fig, ax välja ei tuleks.

plt.tight_layout()

plt.show()