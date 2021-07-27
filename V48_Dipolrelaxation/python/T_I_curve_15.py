import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

t, T, I = np.genfromtxt('data/heizrate_15.csv', comments='#', unpack=True, delimiter=',')
I_offset = 5 #pA
I = -I + I_offset # strom vorzeichen (definition) + offsett
T = T + 273.15 # Kelvin

# Untergrund ausgleichskurve
def f(x, a, b, c):
    return a * np.exp(b*x)+ c

I_unter = np.append(I[0:11], I[32:52])
T_unter = np.append(T[0:11], T[32:52])
print('I_untergrund:', I_unter)
print('T_untergrund:', T_unter)


params, cov = curve_fit(f, T_unter, I_unter, p0=[10**(-5), 0.01, 0.2])
errors = np.sqrt(np.diag(cov))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
c = ufloat(params[2], errors[2])

print('a =', a)
print('b =', b)
print('c =', c)

T_lin = np.linspace(T_unter.min(), T_unter.max(), 1000)

# depolarisationsstrom
I_pol = I[11:32]
T_pol = T[11:32]

#plot
plt.plot(T, I, 'rx', label='Messwerte')
plt.plot(T_unter, I_unter, 'bo', alpha=0.2, label='Teilmenge: Untergrund')
plt.plot(T_pol, I_pol, 'yo', alpha=0.4, label='Teilmenge: Depolarisationsstrom')
plt.plot(T_lin, f(T_lin, *params), label='Ausgleichskurve: Untergrund')

plt.xlabel(r'$T \,/\, K$')
plt.ylabel(r'$I \,/\, pA$')
plt.legend()
plt.tight_layout()

plt.savefig('build/T_I_kurve_15.pdf')
plt.show()