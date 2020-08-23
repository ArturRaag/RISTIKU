# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:05:05 2020

@author: artur
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons, Cursor

plt.style.use("fivethirtyeight")

x=np.arange(-25.0,25.0,0.01)

y1=10+0*x
y2=x
y3=-2*x-5
y4=-10+0*x

fig, ax = plt.subplots()

l0, =ax.plot(x,y1, visible= True, linewidth=3,color="green", label="y = 10") # Why is there a coma after the variable? VASTUS: Koma muudab ta kohe tupleks
l1, =ax.plot(x,y2, lw=3,color="blue", label="y = x")
l2, =ax.plot(x,y3,lw=3,color="red", label="y = -2*x-5")
l3,=ax.plot(x,y4,lw=3, label="y = -10")
lines=[l0, l1, l2, l3]

plt.plot(0,0,marker="o",color="red")
plt.annotate("(0;0)",(0,0))
plt.subplots_adjust(left=0.2)
plt.grid(True)
plt.axis([-20,20,-20,20]) # x-min,x-max, y-min,y-max. Teljed


# Make checkbuttons with all plotted lines with correct visibility

rax = plt.axes([0.05, 0.4, 0.1, 0.15])  # kastikeste asukoht

labels = [str(line.get_label()) for line in lines] # korjame iga joone kohta vajaliku infot(nähtavus ja label), kasutades for tsüklit. Loob listi
visibility = [line.get_visible() for line in lines] # Loob visibility listi
check = CheckButtons(rax, labels, visibility) # CheckButtons funktsioon????? More at matplotlib library

# MIS SEE ON?????
def func(label):
    index=labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()
    
check.on_clicked(func)
cursor=Cursor(ax,horizOn=True,vertOn=True,color="black",lw=3)


plt.show()

