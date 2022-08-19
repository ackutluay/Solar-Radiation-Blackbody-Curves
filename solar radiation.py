# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 15:22:34 2022

@author: ackut
"""

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import Image
from ipywidgets import interact, interactive, fixed, interact_manual, FloatSlider, Layout
import scipy as sp



interact(T=(1,10000))
def wien(T): #Wien displacement law
    b= 2.897771955e-3 #mK
    lmbd= b/T
    print(f"The peak wavelength for temp {T:.0f} K is {lmbd*1e9:.0f} nm")
    
T_Betelgeuse= 3500 #K
T_Rigel= 11e3 #K

wien(T_Betelgeuse), wien(T_Rigel) #for Betelgeuse and Rigel, calculate the peak wavelength.

"""BLACK BODY RADIATION"""

def blackbody(lmbd,T):
    h= 6.62607015e-34 #planck constant #J.s
    c= 299792458.0 #speed of light in m/s
    k= 1.380649e-23 #boltzmann constant in J/K
    a= (2*h*(c**2))/(lmbd)**5
    b= (np.exp(h*c/(lmbd*k*T))-1)
    c= (np.exp(h*c/(lmbd*k*5772))-1) #for the sun
    
    return a/b

lmbd= np.arange(10,4000,1)*1e-9

fig= plt.figure(num=1 , figsize=(5,3))
ax= plt.subplot(xlim=(0,3000),ylim=(0,3))
ax.plot(lmbd*10**9, blackbody(lmbd,5772)/10**13, color="gold")
ax.set_xlabel("Wavelength / nm")
ax.set_ylabel("Spectral Intensity / $10^{13}$ $W/sr.{m^3}$")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()

""" STELLAR LUMINOSITY """

def luminosity(R,T):
    s= 5.670374419*1e-8 #W m^-2 K^-4
    a= 4* np.pi * s
    b= (R**2)*(T**4)
    L=a*b
    return L

Rsun=  6.957*10**8 #m
Tsun= 5772 #K

#input the info of the star.
x= float(input('The radius of the star (Note: If the number is big (probably it is ) use the scientific notation in python "for example 10^32 is 1e32" ) :'))
y= float(input('Temperature of the star: '))    

Lstar= luminosity(x,y)
Lsun= luminosity(Rsun,Tsun)
ratio= Lstar/Lsun #compare a star's luminosity with Sun.

print(ratio)
#By this ratio, you can compare other stars with known radius and temperature, with the Sun.

