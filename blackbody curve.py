# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 16:27:40 2022

@author: ackut
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from IPython.display import Image

def blackbody(lmbd,T):
    h= 6.62607015e-34 #planck constant #J.s
    c= 299792458.0 #speed of light in m/s
    k= 1.380649e-23 #boltzmann constant in J/K
    a= (2*h*(c**2))/(lmbd)**5
    b= (np.exp(h*c/(lmbd*k*T))-1)
    c= (np.exp(h*c/(lmbd*k*5772))-1) #for the sun
    
    return a/b

def wien(T): #Wien displacement law
    b= 2.897771955e-3 #mK
    l= b/T
    return l
    
lmbd= np.arange(10,3000,10)*1e-9 #in meters
t1,t2,t3,t4,t5 = 6000,5000,4000,3000,2000 #temperature's of different arbitrary bodies

temps= np.array([t1,5772,t2,t3,t4,t5])

peaks=[]
spectrals=[]
for i in temps:
    peakL=wien(i)
    BBcurve= blackbody(peakL,i)
    peaks.append(peakL)
    spectrals.append(BBcurve)
    
spectrals = np.array(spectrals)
peaks= np.array(peaks)
 

fig= plt.figure(num=1 , figsize=(10,8))
ax= plt.subplot(xlim=(0,2000),ylim=(0,3.5))
ax.plot(lmbd*10**9, blackbody(lmbd,5772)/10**13, color="gold", label= '5772 K , $\u03BB_{peak}$=502 nm') #wavelength in nm
ax.plot(lmbd*10**9, blackbody(lmbd,t1)/10**13, color="cyan",label= '6000 K , $\u03BB_{peak}$= 483 nm')
ax.plot(lmbd*10**9, blackbody(lmbd,t2)/10**13, color="orange",label= '5000 K , $\u03BB_{peak}$=580 nm')
ax.plot(lmbd*10**9, blackbody(lmbd,t3)/10**13, color="red",label= '4000 K , $\u03BB_{peak}$=724 nm')
ax.plot(lmbd*10**9, blackbody(lmbd,t4)/10**13, color="blue",label= '3000 K , $\u03BB_{peak}$=966 nm')
plt.scatter(peaks*10**9,spectrals/10**13,color="black", s=10, zorder=6)
plt.legend(frameon=False, borderpad=2, labelspacing=1, loc=7, fontsize=14)
ax.set_title('Radiation Curves for Different Temperatures')
ax.set_xlabel("\u03BB / nm")
ax.set_ylabel("Spectral Intensity / $10^{13}$ $W/sr.{m^3}$")
plotText = r"$Planck's\ Law$"+"\n"+r"$B(\lambda,T) = \frac{2hc^2}{\lambda^5} \frac{1}{e^{\frac{hc}{\lambda k_BT}}-1}$"
ax.text(.65, .85, plotText, size=18, va="center", ha="center", multialignment="center", linespacing=2, transform=ax.transAxes)
spectrum = plt.imread("spectrum.png")
ax.imshow(spectrum, extent=[380,740,0,3.5], alpha=0.4)
ax.set_aspect('auto')
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.savefig("blackbodycurves.png")



