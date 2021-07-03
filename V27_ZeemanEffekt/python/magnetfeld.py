import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

I, B = np.genfromtxt('magnetfeld.csv', delimiter=',', unpack=True)

def funktion(x,a,b,c,d):
    return (a*x**3+b*x**2+c*x+d)

params, cov = curve_fit(funktion, I, B)

x_plot = np.linspace(0,5,1000)
print(params)
plt.figure()
plt.plot(I, B, 'x', label='Messwerte')
plt.plot(x_plot, funktion(x_plot, *params), '-', label=r'Ausgleichsfunktion')
plt.xlabel('Stromstärke I / A')
plt.ylabel('Magnetische Flussdichte B / mT')
plt.legend()
plt.grid()
plt.savefig('magnetfeld.pdf')
plt.show()