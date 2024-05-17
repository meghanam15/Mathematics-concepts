import matplotlib.pyplot as plt

# Function to fit a straight line
def fit_line(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(x_i**2 for x_i in x)
    sum_xy = sum(x_i*y_i for x_i, y_i in zip(x, y))
    b = (n*sum_xy - sum_x*sum_y) / (n*sum_x_sq - sum_x**2)
    a = (sum_y - b*sum_x) / n

    return a, b

from tabulate import tabulate


# Input data
n = int(input("Enter the number of data points: "))

# User input for x values
x_values = input("Enter the x values (comma separated): ")
x = list(map(float, x_values.split(',')))

# User input for y values
y_values = input("Enter the y values (comma separated): ")
y = list(map(float, y_values.split(',')))

# Combine x and y into a list of lists
data = [[x[i], y[i]] for i in range(n)]

# Print the table
print(tabulate(data, headers=["X", "Y"], tablefmt="pretty"))


# Fitting the line
a, b = fit_line(x, y)

# Print the equation of the fitted line
print(f"Equation of the fitted line: y = {a:.2f} + {b:.2f}x")

# Plotting
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, [a + b*x_i for x_i in x], color='red', label='Fitted line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fitting a straight line')
plt.legend()
plt.show()
