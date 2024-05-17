import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Define the function to fit (a parabola)
def parabola(x, a, b, c):
    return a * x**2 + b * x + c

n = int(input("Enter the number of data points: "))
# Get data from the user
x_input = input("Enter x values separated by comma: ")
y_input = input("Enter y values separated by comma: ")

x_data = np.array([float(x) for x in x_input.split(",")])
y_data = np.array([float(y) for y in y_input.split(",")])

data = [[x_data[i], y_data[i]] for i in range(n)]
print(tabulate(data, headers=["X", "Y"], tablefmt="pretty"))

# Fit the data using numpy's polyfit
popt, pcov = np.polyfit(x_data, y_data, 2, cov=True)

# Extracting coefficients
a_fit, b_fit, c_fit = popt

# Generate points for plotting the fitted parabola
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = parabola(x_fit, *popt)

print("\nFitted coefficients:")
print("a =", a_fit)
print("b =", b_fit)
print("c =", c_fit)
print("Fitted equation:")
print(f"y = {a_fit:.2f}x^2 + {b_fit:.2f}x + {c_fit:.2f}")

# Plot the original data and the fitted parabola
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_fit, y_fit, color='red', label='Fitted Parabola')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.title('Fitting a Parabola to User Data')
plt.show()
