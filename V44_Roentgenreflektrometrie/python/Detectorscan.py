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

x_plot = np.linspace(-0.5, 0.5, 10000)

#Aus der gauss ausgleichsfkt. das maximum der intensität berechen
I_gauss = gauss(x_plot, *popt)
I_max = np.amax(I_gauss)
index = np.argmax(I_gauss)
x_max = x_plot[index]

#Halbwertsbreite aus ausgleichsfkt. berechnen
half_max = I_max/2
cut_off = np.where(I_gauss >= half_max)
#print(cut_off)
idx_links = np.min(cut_off)
idx_rechts = np.max(cut_off)
print(len(cut_off))
#print(idx_links, idx_rechts)
x_half = [x_plot[idx_links], x_plot[idx_rechts]] 
#print(x_half)
print(abs(x_half[0]- x_half[1]))

#plotten
plt.figure()
plt.plot(theta, I, 'rx',label='Messwerte')
plt.plot(x_max, I_max,'ko' ,label='Intensitätsaximum')
plt.plot(x_half, gauss(x_half, *popt), '--', label='Halbwertsbreite')
plt.plot(x_plot, gauss(x_plot, *popt), 'b-',label='Gaußfunktion')
plt.grid()
plt.legend()
plt.xlabel(r'$\theta$')
plt.ylabel('Intentsität')
plt.savefig('Detectorscan.pdf')