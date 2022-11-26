import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
y = [5.7, 16.6, 58.0, 278.9, 1069.3, 3181.4, 7844.3, 16883.9, 32854.9, 59144.2, 100106.7, 161166.3, 248958.6]

fig, ax = plt.subplots(figsize = (12,6))

ax.plot(x, y, "k.")
plt.show()
plt.close()


polynomial_coeff = np.polyfit(x,y,2)
print(polynomial_coeff)

xnew= np.linspace(2,20,100)
ynew = np.poly1d(polynomial_coeff)
fig, ax = plt.subplots(figsize = (12,6))
ax.plot(xnew,ynew(xnew),x,y,'o')
plt.show()
plt.close()


