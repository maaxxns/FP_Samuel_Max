import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

data = np.genfromtxt('data/zscan_0.UXD')

z = data[15:43,0]
I = data[15:43,1]

def fun(x,a,b,c):
    return a * np.tanh(b*x) + c

#popt, cov = curve_fit(fun, z, I)

z_plot = np.linspace(np.min(z), np.max(z), 10000)


print('Strahlbreite in mm: ', abs(data[32, 0]-data[26, 0]))

plt.plot(z, I, 'rx', label='Messdaten')
plt.axvline(data[32,0], color='green', label='Strahlbreite')
plt.axvline(data[26,0], color='green')
#plt.plot(z_plot, fun(z_plot, *popt), '-', label='Ausgleichsfuniktion')
plt.xlabel(r'$z \, / \, \si{\milli\meter}$')
plt.ylabel('Intensität')
plt.grid()
plt.legend()
plt.savefig('build/zscan.pdf')

