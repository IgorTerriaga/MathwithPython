import matplotlib.pyplot as plt
import numpy as np


def f(t): return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.linspace(5, 10, num=100)
yt1 = f(t1)
t2 = np.linspace(5, 25, num=100)
yt2 = f(t2)

plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(t1, yt1, 'bo', t2, yt2, 'k')
plt.subplot(2, 1, 2)
ycos = np.cos(2*np.pi*t2)
plt.plot(t2, ycos, 'r--')
plt.show()
