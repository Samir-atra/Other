# This script demonstrates polynomial curve fitting using numpy and matplotlib.

import matplotlib.pyplot as plt
import numpy as np

# Sample data points
x_values = [0.05, 0.1, 0.15, 0.2, 0.25, 0.28, 0.29, 0.3, 0.31, 0.35, 0.4, 0.45, 0.5, 0.55]
y_values = [0.00103, 0.000953, 0.00081, 0.00073, 0.000692, 0.000659, 0.00066, 0.000671, 0.000693, 0.000688, 0.000812, 0.000928, 0.001075, 0.001228]

# Fit a 2nd-degree polynomial to the data
# The result 'values' is an array of coefficients [c2, c1, c0] for the polynomial c2*x^2 + c1*x + c0
values = np.polyfit(x_values, y_values, 2)
print("Polynomial coefficients:", values)

# Use the pre-calculated coefficients for plotting
# Note: It's generally better to use the 'values' calculated by polyfit.
# This seems to be a pre-computed or alternative set of coefficients.
z = np.array([ 0.00756766, -0.0041761,  0.00125393])

# Generate x-values for the fitted curve to create a smooth line
x2 = np.linspace(0, 0.7, 100) # Increased points for a smoother curve

# Plot the fitted polynomial curve
plt.plot(x2, np.polyval(z, x2), label="Fitted Curve")

# Plot the original data points as a scatter plot
plt.scatter(x_values, y_values, color='r', label="Original Data")

# Add titles and labels for clarity
plt.title("Polynomial Curve Fitting")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
