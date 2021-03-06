import numpy as np
from matplotlib import pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit

# values
t, T, I = np.genfromtxt('data/heizrate_20.csv', comments='#', unpack=True, delimiter=',')
I_offset = 3.5 #pA
I = -I + I_offset # strom vorzeichen (definition) + offsett
I = I * 10**(-12) #ampere
T = T + 273.15 # Kelvin

# d = 3 * 10**(-3) # m
# A = np.pi * (d/2)**2
# I= I / A 

k_B = 1.380649 * 10**(-23) #J/K
e_volt = 1.602176634 * 10**(-19) #J
a_unt = 6e-06
b_unt = 0.0502
c_unt = 0.73

def f(x, a, b, c):
    return a * np.exp(b*x)+ c

def I_func(T, a, W):
    return a * np.exp(-W / (k_B *T))

I_dep = I[11:19] - f(T[11:19], a_unt, b_unt, c_unt)*10**(-12) #ampere
print(I_dep)
T_dep = T[11:19]

params, cov = curve_fit(I_func, T_dep, I_dep, p0=[1, 10**(-19)])
errors = np.sqrt(np.diag(cov))
W = ufloat(params[1], errors[1])
print(f'Aktivierungsenergie W = {W}J = {W/e_volt}eV')

T_lin = np.linspace(T_dep.min(), T_dep.max(), 10000)
plt.semilogy(T_dep, I_dep, 'rx', label='Messwerte')
plt.semilogy(T_lin, I_func(T_lin, *params), label='Ausgleichsfunktion')
plt.xlabel(r'$T \,/\, K$')
plt.ylabel(r'$I \,/\, pA$')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('build/W_approx_20.pdf')
plt.show()