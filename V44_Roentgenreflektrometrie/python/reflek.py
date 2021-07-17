import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Daten einlesen, I_max aus Detectorscan
data_dif = np.genfromtxt('data/Omega2ThetaScan2_difuse.UXD', unpack = True)
data_ref = np.genfromtxt('data/Omega2ThetaScan2.UXD', unpack = True)
I_max = 1637959.6850157096 *5 #mal fünf wegen unterschiedlicher messzeiten
                              #beim Detectorscan 1s hier 5s
#a_g = #Geometriewinkel
#d_0 = #Strahlbreite
#G = #Geometriefaktor


#x_dif und x_ref sind im Grunde das selbe also wird im weiteren verlauf nur eins genutzt
x_dif = data_dif[:, 0]
x_ref = data_ref[:, 0]
x = x_ref[1:(len(x_ref)-1)] #schneiden ersten und letzten wert ab um teilen durch null zu verhindern

I_dif = data_dif[1:(len(x_ref)-1), 1]#hier auch teilen durch null verhindern
I_ref = data_ref[1:(len(x_ref)-1), 1]

R_dif = I_dif / I_max
R_ref = I_ref / I_max
 
R_abs = R_ref - R_dif
print(R_abs, R_abs.shape)
#R_G = R_abs*G #Korrektur geometriewinkel

# Ideale Fresnelreflektivität
a_c_Si = 0.223
R_ideal = (a_c_Si / (2 * x))**4

plt.figure()
plt.plot(x, R_dif/10, label='Diffuser Scan / 10')
plt.plot(x, R_ref/10, label='Reflektivitätsscan / 10')
plt.plot(x, R_abs, label='Reflektivität')
plt.plot(x, R_ideal, label='Ideal Reflektivität')
plt.grid()
plt.yscale('log')
plt.legend()
plt.xlabel(r'$\alpha_i$')
plt.ylabel(r'$R$')
plt.savefig('reflek.pdf')
plt.show()