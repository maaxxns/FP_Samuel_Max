import numpy as np 
import matplotlib.pyplot as plt
from uncertainties.unumpy import uarray
import uncertainties
#Einlesen
ordnung_rot, delta_s_rot, kronika_s_rot = np.genfromtxt('pixel_values_rot_sigma_maxzumax.csv', delimiter=',', unpack=True)
ordnung_blau_pi, delta_s_blau_pi, kronika_s_blau_pi = np.genfromtxt('pixel_values_pi_blau.csv', delimiter=',', unpack=True)
ordnung_blau_sigma, delta_s_blau_sigma, kronika_s_blau_sigma = np.genfromtxt('pixel_values_sigma_blau.csv', delimiter=',', unpack=True)

#funktion zur berechnung der wellenlängen verschiebung
def delta_lam(delta_s, lambda_ , kronika_s):
    d = 4 *10**6
    n =  1.4567
    delta_s = uarray(delta_s, [2]*len(delta_s))
    kronika_s = uarray(kronika_s, [2]*len(delta_s))
    lamnda_disp = (lambda_**2)/(2*d) * np.sqrt(1/(n**2 -1))
    return 1/2 *(kronika_s)/(delta_s) *lamnda_disp

def g_ij(delta_lam, lambda_, B):
    y_b = 9.274 * 10**(-24)
    h = 6.626 * 10**(-34)
    c = 299_792_458
    return delta_lam*10**(-9) * (h*c) /(y_b * B *(lambda_*10**(-9))**2)

print('verschiebung rot: ', (delta_lam(delta_s_rot, 643.8 ,kronika_s_rot)))
print('verschiebung blau_pi: ', delta_lam(delta_s_blau_pi, 480 ,kronika_s_blau_pi))
print('verschiebung blau_sigma: ', delta_lam(delta_s_blau_sigma, 480 ,kronika_s_blau_sigma))

print('g_ij für rot : ', g_ij(np.sum(delta_lam(delta_s_rot, 643.8 ,kronika_s_rot)/10), 643.8, 0.443))
print('g_ij für blau_pi : ', g_ij(np.sum(delta_lam(delta_s_blau_pi, 480 ,kronika_s_blau_pi)/11), 480, 0.443))
print('g_ij für blau_sigma : ', g_ij(np.sum(delta_lam(delta_s_blau_sigma, 480 ,kronika_s_blau_sigma)/11), 480, 0.365))

delta_lam_rot = delta_lam(delta_s_rot, 643.8 ,kronika_s_rot)
delta_lam_blau_pi = delta_lam(delta_s_blau_pi, 480 ,kronika_s_blau_pi)
delta_lam_blau_sigma = delta_lam(delta_s_blau_sigma, 480 ,kronika_s_blau_sigma)

plt.figure()
plt.plot(ordnung_rot, delta_s_rot, 'x', label=(r'$\Delta s \, rot -\sigma$'))
plt.plot(ordnung_rot, kronika_s_rot, 'o', label=r'$\delta s \,rot -\sigma$')
plt.legend()
plt.xlabel('Ordnung')
plt.ylabel('Anzahl Pixel')
plt.grid()
plt.savefig('Rot_messwerte.pdf')
plt.show()

plt.figure()
plt.plot(ordnung_blau_pi, delta_s_blau_pi, 'x', label=r'$\Delta s \,Blau- \pi$')
plt.plot(ordnung_blau_pi, kronika_s_blau_pi, 'o', label=r'$\delta s \, Blau-\pi$')
plt.legend()
plt.xlabel('Ordnung')
plt.ylabel('Anzahl Pixel')
plt.grid()
plt.savefig('blau_pi_messwerte.pdf')
plt.show()

plt.figure()
plt.plot(ordnung_blau_sigma, delta_s_blau_sigma, 'x', label=r'$\Delta s \,Blau- \sigma$')
plt.plot(ordnung_blau_sigma, kronika_s_blau_sigma, 'o', label=r'$\delta s \, Blau- \sigma$')
plt.legend()
plt.xlabel('Ordnung')
plt.ylabel('Anzahl Pixel')
plt.grid()
plt.savefig('blau_sigma_messwerte.pdf')
plt.show()

plt.figure()
plt.errorbar(ordnung_rot, uncertainties.unumpy.nominal_values(delta_lam_rot), fmt='_',yerr=uncertainties.unumpy.std_devs(delta_lam_rot), label=r'$\Delta \lambda \,Rot-\sigma$' )
plt.legend()
plt.xlabel('Ordnung')
plt.ylabel('Verschiebung in nm')
plt.grid()
plt.savefig('Rot_verschiebung.pdf')
plt.show()

plt.figure()
plt.errorbar(ordnung_blau_pi, uncertainties.unumpy.nominal_values(delta_lam_blau_pi), fmt='_',yerr=uncertainties.unumpy.std_devs(delta_lam_blau_pi), label=r'$\Delta \lambda \,Blau-\pi$' )
plt.legend()
plt.xlabel('Ordnung')
plt.ylabel('Verschiebung in nm')
plt.grid()
plt.savefig('blau_pi_verschiebung.pdf')
plt.show()

plt.figure()
plt.errorbar(ordnung_blau_sigma, uncertainties.unumpy.nominal_values(delta_lam_blau_sigma), fmt='_',yerr=uncertainties.unumpy.std_devs(delta_lam_blau_sigma), label=r'$\Delta \lambda \,Blau-\sigma$' )
plt.legend()
plt.xlabel('Ordnung')
plt.ylabel('Verschiebung in nm')
plt.grid()
plt.savefig('blau_sigma_verschiebung.pdf')
plt.show()