# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:51:41 2020

@author: artur
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

palk=570
kulu_päevas=10
üür=160

x=np.arange(0,31)

jaak=palk-üür-kulu_päevas*x

plt.plot(x,jaak)
plt.ylabel("y-telg")
plt.xlabel("x-telg")
plt.plot(0,0,marker="o",color="red")
plt.annotate("0-punkt", (0,0))

plt.grid(True)
plt.show()


