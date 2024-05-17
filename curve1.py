import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Define the function to fit (a curve of the form y = ab^x)
def power_curve(x, a, b):
    return a * np.power(b, x)

n = int(input("Enter the number of data points: "))
# Get data from the user
x_input = input("Enter x values separated by comma: ")
y_input = input("Enter y values separated by comma: ")

x_data = np.array([float(x) for x in x_input.split(",")])
y_data = np.array([float(y) for y in y_input.split(",")])

data = [[x_data[i], y_data[i]] for i in range(n)]
print(tabulate(data, headers=["X", "Y"], tablefmt="pretty"))

# Linearize the model: y = ab^x => log(y) = log(a) + x * log(b)
log_y_data = np.log(y_data)

# Perform linear regression
coefficients = np.polyfit(x_data, log_y_data, 1)

# Extracting coefficients
log_b_fit, log_a_fit = coefficients
a_fit = np.exp(log_a_fit)
b_fit = np.exp(log_b_fit)

# Generate points for plotting the fitted curve
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = power_curve(x_fit, a_fit, b_fit)

print("\nFitted coefficients:")
print("a =", a_fit)
print("b =", b_fit)
print("Fitted equation:")
print(f"y = {a_fit:.2f} * {b_fit:.2f}^x")

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_fit, y_fit, color='red', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.title('Fitting a Power Curve (y = ab^x) to User Data')
plt.show()
