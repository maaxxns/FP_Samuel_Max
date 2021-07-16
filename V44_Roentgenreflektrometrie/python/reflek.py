import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Daten einlesen
data_dif = np.genfromtxt('data/Omega2ThetaScan2_difuse.UXD')
data_ref = np.genfromtxt('data/Omega2ThetaScan2.UXD')


#x_dif und x_ref sind im Grunde das selbe also wird im weiteren verlauf nur eins genutzt
x_dif = data_dif[:, 0]
x_ref = data_ref[:, 0]
x = x_ref

I_dif = data_dif[:, 1]
I_ref = data_ref[:, 1]

I_abs = I_ref - I_dif

plt.figure()
plt.plot(x, I_abs, label='Reflektivität')
plt.grid()
plt.yscale('log')
plt.legend()
plt.xlabel('x?')
plt.ylabel('Inensität?')
plt.savefig('reflek.pdf')
plt.show()