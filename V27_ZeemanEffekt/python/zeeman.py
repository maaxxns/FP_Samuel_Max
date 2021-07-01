import numpy as np 
import matplotlib.pyplot as plt
from uncertainties.unumpy import uarray

#Einlesen
ordnung_rot, delta_s_rot, kronika_s_rot = np.genfromtxt('pixel_values_pi_rot.csv', delimiter=',', unpack=True)
ordnung_blau_pi, delta_s_blau_pi, kronika_s_blau_pi = np.genfromtxt('pixel_values_pi_blau.csv', delimiter=',', unpack=True)
ordnung_blau_sigma, delta_s_blau_sigma, kronika_s_blau_sigma = np.genfromtxt('pixel_values_sigma_blau.csv', delimiter=',', unpack=True)

#funktion zur berechnung der wellenlängen verschiebung
def delta_lam(delta_s, lambda_ , kronika_s):
    d = 4 *10**6
    n =  1.4567
    delta_s = uarray(delta_s, [5]*len(delta_s))
    kronika_s = uarray(kronika_s, [5]*len(delta_s))
    lamnda_disp = (lambda_**2)/(2*d) * np.sqrt(1/(n**2 -1))
    return 1/2 *np.sum(kronika_s)/np.sum(delta_s) *lamnda_disp

print('verschiebung rot: ', delta_lam(delta_s_rot, 643.8 ,kronika_s_rot))
print('verschiebung blau_pi: ', delta_lam(delta_s_blau_pi, 643.8 ,kronika_s_blau_pi))
print('verschiebung blau_sigma: ', delta_lam(delta_s_blau_sigma, 643.8 ,kronika_s_blau_sigma))