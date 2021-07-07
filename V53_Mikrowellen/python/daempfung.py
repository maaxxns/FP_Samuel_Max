import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

def f(x, a, b, c):
    return a*x**2 + b*x + c

d = np.array([2.8, 3.05, 3.21, 3.4, 3.5, 3.7]) #mm
daempfung = np.array([0, 2, 4, 6, 8, 10]) #dB

# theorie kurve (fit)
d_theorie = np.array([0, 0.9, 1.4, 1.75, 2.05, 2.3])
params, covariance_matrix = curve_fit(f, d_theorie, daempfung)
d_lin = np.linspace(2.0, 5.0, 1000)
errors = np.sqrt(np.diag(covariance_matrix))

print('parameter:', params)
print('cov:', errors)
print('verschiebung:', f(d, *params)-daempfung)
verschiebung = np.mean(f(d, *params)-daempfung)
print('verschiebung_mittelwert:', verschiebung)

plt.figure()
plt.plot(d, daempfung, 'b.', label = 'Messwerte')
plt.plot(d, daempfung+verschiebung, 'gx', label = 'Messwerte verschoben')
plt.plot(d_lin, f(d_lin, *params), 'r-', label = 'Theorie')

plt.xlabel('$x \,/\, mm$')
plt.ylabel('Dämpfung $\,/\, dB$')
plt.legend()
plt.tight_layout()
plt.savefig('build/daempfung.pdf')
plt.show()