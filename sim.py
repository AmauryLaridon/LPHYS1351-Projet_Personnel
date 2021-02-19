import matplotlib.pyplot as plt
import numpy as np
import math


mu = np.linspace(0, 1, 100)
mu2 = np.linspace(0, 1.5, 150)


def rho_pl(lam, x):
    y = (lam-1)+math.sqrt((lam-1)**2+4*(1-x))
    y = y/2
    return y


def rho_min(lam, x):
    y = (lam-1)-math.sqrt(((lam-1)**2)+4*(1-x))
    y = y/2
    return y


rho_plus1 = []
rho_plus0 = []
rho_plus2 = []
rho_moins = []
l1 = 1
l0 = 0.5
l2 = 1.4

for i in range(100):
    rho_plus1.append(rho_pl(l1, mu[int(i)]))
    rho_plus0.append(rho_pl(l0, mu[int(i)]))
for i in range(150):
    rho_plus2.append(rho_pl(l2, mu2[int(i)]))


plt.plot(mu, rho_plus1, label='lambda = 1')
plt.plot(mu, rho_plus0, label=' lambda < 1')
plt.plot(mu, rho_plus2, label='lambda > 1')
plt.legend()

plt.show()
