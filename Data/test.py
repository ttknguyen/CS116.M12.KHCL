import numpy as np 
import matplotlib.pyplot as plt

x = np.array(range(-10, 11))
y = x ** 2

print('x:', x)
print('y:', y)

plt.plot(x, y)

for i in x:
    plt.plot(i, i ** 2, 'ro')
    plt.pause(0.5)

plt.show()