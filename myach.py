import numpy as np
import matplotlib.pyplot as plt

#Константы и начальные значения
m = 10.0
k = 2.0
g = 9.81
h0 = 0.5
v0 = 0.0
t_end = 2*np.sqrt(m/k)
dt = 0.001
#Хранение результатов
t = np.arange(0, t_end, dt)
h = np.zeros_like(t)
h[0] = h0
v = v0
#Моделирование
for i in range(1, len(t)):
    Ft = m*g
    Fu = k*h[i-1]
    Fn = Ft - Fu
    a = Fn/m
    v = v+a*dt
    h[i] = h[i-1] + v*dt
plt.plot(t, h)
plt.xlabel("Время, секунды")
plt.ylabel("Высота, метры")
plt.show()

