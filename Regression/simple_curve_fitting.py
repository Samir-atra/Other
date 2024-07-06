import matplotlib.pyplot as plt
import numpy as np

x_values = [0.05, 0.1, 0.15, 0.2, 0.25, 0.28, 0.29, 0.3, 0.31, 0.35, 0.4, 0.45, 0.5, 0.55]
y_values = [0.00103, 0.000953, 0.00081, 0.00073, 0.000692, 0.000659, 0.00066, 0.000671, 0.000693, 0.000688, 0.000812, 0.000928, 0.001075, 0.001228]

values = np.polyfit(x_values,y_values,2)

z = np.array([ 0.00756766, -0.0041761,  0.00125393])
x2 = np.linspace(0, 0.7, 20)

plt.plot(x2, np.polyval(z, x2))
plt.scatter(x_values,y_values,color='r')
plt.show()
