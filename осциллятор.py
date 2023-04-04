import numpy as np
import matplotlib.pyplot as plt

a = 0.1

def s(k):
    return np.sin(k)

def n(k):
    length = k.shape[0]
    u, d = 0, 0.05
    noise = np.random.normal(u, d, size=length)
    return noise

k = np.arange(0, 5*np.pi, 0.1)
S = s(k)
D = S + n(k)
F = D +  a
plt.plot(k, s(k), color='blue', label="s(k)")
plt.plot(k, s(k)+n(k), label='s(k)+n(k)')
plt.plot(k, s(k)+n(k)+a, label='s(k)+n(k)+a')
plt.legend(loc='best')
plt.xlabel('k')
plt.ylabel('v')
plt.title("")
plt.show()
