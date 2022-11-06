import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Below code plots two absolute functions
# f(x) = |x| and f(x) = -|x|
# Positive - will open above 0 on the y axis
# Negative - will open below 0

def pos_neg(n):

    x = np.arange(-n, n+1)
    y = -(np.abs(x))
    plt.plot(x, y)


    y = (np.abs(x))
    fig = plt.figure
    ax = plt.subplot(111)
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    plt.plot(x, y)
    plt.show() 
    plt.close()

pos_neg(25)

# General form of equation - f(x) = a|x - h| + k
# Where a tells us how far graph opens up, and whether it opens up positively or negatively
# |x| is the absolute value of x
# h and k are how far graph shifts horizontally or vertically
# Below example graphs -2|x| + 4
# Value of a is -2, which means graph will open downwards
# h value is 0 and k value is 4 - will shift by 4 points to the right
# For this example, assume x is 10


def plot_abs_value(n, h, k, a, pos = True):
    x = np.arange(-n, n+1)
    if pos == True:
        y = a * (abs(x - h) + k)
    else:
        y = -a * (abs(x - h) + k)
    
    return x,y

x, y = plot_abs_value(2, 0, 0, 3, pos = True)
x2,y2 = plot_abs_value(2, 0, 0, 1, pos = True)

fig = plt.figure
ax = plt.subplot(111)
line1 = ax.plot(x,y, label = "f(x) = 3|2 - 0| + 0")
line2 = ax.plot(x2,y2, label = "f(x) = 1|2 - 0| + 0")

ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.legend()
plt.show()
plt.close()

