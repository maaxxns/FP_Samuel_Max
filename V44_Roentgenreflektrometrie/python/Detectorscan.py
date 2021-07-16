import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Daten einlesen
data = np.genfromtxt('data/detectorscan.UXD')

theta= data[:,0]
I = data[:, 1]

#gauss funktion def.

def gauss(x, a, sigma, mu):
    # print(sigma)
    return a*np.exp(- (x-mu)**2 / 2*sigma**2)

#curve_fit machen
popt, cov = curve_fit(gauss, theta, I, p0=(1,1,1) )

x_plot = np.linspace(-0.5, 0.5, 1000)

#plotten
plt.figure()
plt.plot(theta, I, 'rx',label='Messwerte')
plt.plot(x_plot, gauss(x_plot, *popt), 'b-',label='Gaußfunktion')
plt.grid()
plt.legend()
plt.xlabel(r'$\theta$')
plt.ylabel('Intentsität')
plt.savefig('Detectorscan.pdf')