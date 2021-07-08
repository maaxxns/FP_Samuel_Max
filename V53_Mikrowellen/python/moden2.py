#data
daempfung = 30 #db

#1. modus
V0_1 = 220 #V
V1_1 = 205
V2_1 = 240
A0_1 = 31.25 #V
f0_1 = 9010 #MHz
x1 = -0.10416667
y1 = 46.354166667
z1 = -5125

#2. modus
V0_2 = 140 #V
V1_2 = 120
V2_2 = 150
A0_2 = 21.25 #V
f0_2 = 9013 #MHz
x2 = -0.10625
y2 = 28.6875
z2 = -1912.5

#3. modus
V0_3 = 85 #V
V1_3 = 70
V2_3 = 95
A0_3 = 17 #V
f0_3 = 9020 #MHz
x3 = -17/150
y3 = 187/10
z3 = -2261/3

#plot
import matplotlib.pyplot as plt
import numpy as np

def f(U, x, y, z):
    return x*U**2 + y*U + z

U_lin = np.linspace(60, 250, 1000)

ax = plt.subplot(111)

#fit
ax.plot(U_lin, f(U_lin, x1, y1, z1), color='red', label='1. Mode')
ax.plot(U_lin, f(U_lin, x2, y2, z2), color='blue', label='2. Mode')
ax.plot(U_lin, f(U_lin, x3, y3, z3), color='green', label='3. Mode')

# measured values
ax.plot([V0_1, V1_1, V2_1], [A0_1, 0, 0], 'rx')
ax.plot([V0_2, V1_2, V2_2], [A0_2, 0, 0], 'bx')
ax.plot([V0_3, V1_3, V2_3], [A0_3, 0, 0], 'gx')

# axis
ax.set_ylim(bottom=0)
ax.set_ylim(top=35.0)

ax.set_xlabel('$U \, / \, V$')
ax.set_ylabel('$A \, / \, V$')

ax.grid()
ax.legend()
plt.tight_layout()
plt.savefig('build/moden.pdf')
plt.show()