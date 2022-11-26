import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
y = [1.3, 1.2, 9.4, 27.3, 63.1, 126.5, 217.3, 341.5, 512.8, 729.3, 1001.8, 1332.7, 1728.9, 2198.8, 2743.7, 3376.7]

fig, ax = plt.subplots(figsize = (12,6))

ax.plot(x, y, "k.")
plt.show()
plt.close()


polynomial_coeff = np.polyfit(x,y,3)
print(polynomial_coeff)

xnew= np.linspace(2,20,100)
ynew = np.poly1d(polynomial_coeff)
fig, ax = plt.subplots(figsize = (12,6))
ax.plot(xnew,ynew(xnew),x,y,'o')
plt.show()
plt.close()


