import streamlit as st
import pandas as pd
import pytransit as pytr
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci


st.write("Hello World")

"""
# My first app
Here's our first attempt at using data to create a table:
"""

import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

#Initialize figure
plt.figure(figsize=(13,5))

#Swipe function from quickstart guide for pytransit module
#Convuluted way to plot perhaps, but given in quickstart guide so running for now
def plot_lc(time, flux, c=None, ylim=(0.9865, 1.0025), ax=None):
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig, ax = None, ax
    ax.plot(time, flux, c=c)
    ax.autoscale(axis='x', tight=True)
    plt.setp(ax, xlabel='Time [d]', ylabel='Flux', xlim=time[[0,-1]], ylim=ylim)

    if fig is not None:
        fig.tight_layout()
    return ax

#Road runner module (suitable for most use cases)
tm = pytr.RRModel('power-2')
tm.set_data(time = np.linspace(-0.05, 0.05, 500))



flux = tm.evaluate(k=0.1, ldc=[0.6, 0.5], t0=0.0, p=1, a=4.2, i=0.5*np.pi, e=0.0, w=0.0)
plot_lc(tm.time, flux);

#k = planet-star radius ratio
#ldc = limb darkening model coefficients 
#t0 = the zero epoch
#p = the orbital period
#a = the orbital semi-major axis divided by the stellar radius
#i = the orbital inclination in radians
#e = the orbital eccentricity (optional, can be left out if assuming circular a orbit, which we probably will)
#w = the argument of periastron in radians (also optional, can be left out if assuming circular a orbit, which we probably will).

plt.show
