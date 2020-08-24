# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:17:03 2020

@author: artur
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons, Cursor

###########################[ F U N K T S I O O N I D ] ####################################
x=np.arange(-10.0,10.0,0.1)
y1="x"
y2="-2*x**2"
y3="3*x**2-3*x-25"
# Kui soovid juurde lisada, siis täienda all pool Check Buttons funktsiooni.
######################[ F U N K T S I O O N I D ] ##########################################

plt.style.use("classic")
fig,ax = plt.subplots()

# Nihutan vasaku ja alumise telje null-punkti.
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))

# Eemaldan ülemise ja parema telje.
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Lisan telgedele nooled.
ax.plot(1,0,">", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0,1,"^",transform=ax.get_xaxis_transform(), clip_on=False)

# GRAAFIKU ILLUSTREERIMINE
plt.plot(0,0,marker="o",color="red") # Siin kohas võid ka vajadusel graafikule üksikuid punkte lisada.
plt.annotate("(0;0)",(0,0)) 
plt.subplots_adjust(left=0.2)
plt.grid(True,linestyle="-.")
plt.xlim(-25.0,25.0)
plt.ylim(-35.0,25.0)

# CHECK BUTTONS FUNCTION. Kui lisad y=f(x)'e juurde siis pead seda täiendama...
l1,=ax.plot(x,eval(y1),visible=False,lw=3,color="blue",label=(y1))
l2,=ax.plot(x,eval(y2),visible=False,lw=3,color="red",label=(y2))
l3,=ax.plot(x,eval(y3),visible=True,lw=3,color="green",label=(y3))

lines=[l1,l2,l3]


# Kasti asukoht ja funktsioon mis selle tööle paneb.
nupude_kast = plt.axes([0.05,0.4,0.1,0.15]) # sammud: RIGHT, UP, LEFT, DOWN

labels=[str(line.get_label()) for line in lines]
visibility=[line.get_visible() for line in lines]
check = CheckButtons(nupude_kast, labels, visibility)

def func(label):
    index=labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()
    
check.on_clicked(func)

# CURSOR

cursor=Cursor(ax,horizOn=True,vertOn=True,color="cyan",lw=1)

plt.show()