import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

data = np.genfromtxt('data/rocking_curve_0.UXD', unpack=True)

#Geometriewinkel ablesen:
index = [11,39]
a_g = np.mean(np.abs(data[0, index]))
print('geometriewinkel, links, rechts: ', data[0,index],' Geometriewinelmittel: ', a_g)


plt.plot(data[0,:], data[1,:], 'rx', label='Messdaten')
plt.axvline(data[0,11], color='green', label='Geometriewinkel')
plt.axvline(data[0,39], color='green')
#plt.plot(z_plot, fun(z_plot, *popt), '-', label='Ausgleichsfuniktion')
plt.xlabel(r'$\alpha_\text{i} \, / \, \si{\degree}$')
plt.ylabel('Intensität')
plt.grid()
plt.legend()
plt.savefig('build/rockingscan.pdf')
