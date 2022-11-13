import numpy as np
from numpy import random
import scipy.stats as stats
import matplotlib.pyplot as plt
import scipy.optimize as so

x = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
y = [0.7, 1.1, 1.5, 1.6, 1.7, 2.0, 2.3, 2.4, 2.2, 2.1, 2.4, 2.6, 2.2, 2.7, 2.5, 2.7, 2.8, 2.9, 3.1]

x = np.array(x)
y = np.array(y)


# Method 1

best_fit_poly = np.polyfit(x,y,1)
poly_m = best_fit_poly[0]
poly_c = best_fit_poly[1]

# Method 2

def cost(MC):
    m,c = MC
    cost = np.sum((y-m*x-c) ** 2)
    return cost

result = so.minimize(cost, (2.0, 2.0))
opt_m = result.x[0]
opt_c = result.x[1]

# Method 3
def f(m,x,c):
    return m*x+c

result = so.curve_fit(f,x,y)
curve_m, curve_c = result[0]
print(curve_m, curve_c)


# Plotting resulting lines with original data
plt.plot(x,y, 'k.', label = "Original Data")
plt.plot(x, poly_m * x + poly_c, 'r-', label = "Polyfit")
plt.plot(x, opt_m * x + opt_c, 'b-', label = "Optimize")
plt.plot(x, curve_m * x + curve_c, 'g-', label = "Curve Fit")
plt.legend()
plt.show()

