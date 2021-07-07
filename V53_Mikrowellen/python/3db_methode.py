import numpy as np

d1 = 63.3 # mm
d2 = 65.3
min1 = 72.9
min2 = 48.8

lam = (min1-min2)*2
print('lam =', lam)
S = np.sqrt(1 + 1/(np.sin((np.pi*(d2-d1))/lam)**2))
print('S =', S)

S_naeherung = lam / (np.pi * (d2 - d1))
print('S_naeherung = ', S_naeherung)