f_a = 9010 #Hz
f_b = 8989
f_c = 9029

U_a = 220 #V
U_b = 210
U_c = 230

print('elektronische Bandbreite:', f_c-f_b)
print('Abstimm-Empfindlichkeit:', (f_c-f_b)/(U_c-U_b))