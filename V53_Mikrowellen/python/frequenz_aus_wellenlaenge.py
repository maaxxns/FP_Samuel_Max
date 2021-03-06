import numpy as np
c = 299792458 # m/s
lam = 50 *10**(-3) #m
a = 22.86 * 10**(-3) #m
f = c * np.sqrt((1/lam)**2 + (1/(2*a)**2))
print('f =', f*10**(-9), 'GHz')

f_gem = 9007 * 10**6 #Hz

print(f'v_phase = {f_gem*lam} m/s = {f_gem*lam/c} c')