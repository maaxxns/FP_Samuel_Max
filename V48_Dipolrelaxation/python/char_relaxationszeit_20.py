import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

t, T, I = np.genfromtxt('data/heizrate_20.csv', comments='#', unpack=True, delimiter=',')
T = T + 273.15 # Kelvin
t = t*60 #s

def f(x, a, b):
    return a*x + b

# Berechne durchschnittliche heizrate
params, cov = curve_fit(f, t, T)
errors = np.sqrt(np.diag(cov))
b = ufloat(params[0], errors[0]) #heizrate
T_0 = ufloat(params[1], errors[1])

print(f'b = {b} K/s = {b*60} K/min')
print(f'T_0 = {T_0}')

# Berechnung char. relaxationszeit
k_B = 1.380649 * 10**(-23) #J/K
T_max = 262 #K
W_int = ufloat(1.412*10**(-19),0.029*10**(-19))
W_approx = ufloat(9.6*10**(-20), 0.5*10**(-20))

tau_max_approx = k_B * T_max**2 / (b*W_approx)
tau_max_int = k_B * T_max**2 / (b*W_int)
print(f'tau_int = {tau_max_int} s')
print(f'tau_approx = {tau_max_approx} s')

tau_0_approx = tau_max_approx * unp.exp(-W_approx / (k_B*T_max))
tau_0_int = tau_max_int * unp.exp(-W_int / (k_B*T_max))

print(f'tau_0 für approx: {tau_0_approx}')
print(f'tau_0 für int: {tau_0_int}')

# Plot
plt.plot(t/60, T, 'rx', label='Messwerte')
plt.plot(t/60, f(t, *params), label='Ausgleichsgerade')
plt.ylabel(r'$T \,/\, K$')
plt.xlabel(r'$t \,/\, min$')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('build/char_relaxationszeit_20.pdf')
plt.show()