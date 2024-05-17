import matplotlib.pyplot as plt
import numpy as np

# Function to calculate mean
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Function to calculate standard deviation
def calculate_standard_deviation(numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

# Function to calculate correlation coefficient
def calculate_correlation_coefficient(data1, data2):
    mean1 = calculate_mean(data1)
    mean2 = calculate_mean(data2)
    std_dev1 = calculate_standard_deviation(data1)
    std_dev2 = calculate_standard_deviation(data2)
    correlation_coefficient = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2)) / len(data1) / std_dev1 / std_dev2
    #print(mean1,mean2,std_dev2,std_dev1,correlation_coefficient)
    return correlation_coefficient

from tabulate import tabulate
n = int(input("Enter the number of values "))
# User input
data1 = input(f"Enter {n} x values (comma separated): ")
data1 = list(map(float, data1.split(',')))
data2 = input(f"Enter {n} y values (comma separated): ")
data2 = list(map(float, data2.split(',')))

# Combine data1 and data2 into a list of lists
table_data = [[i+1, data1[i], data2[i]] for i in range(n)]

# Print the table
print(tabulate(table_data, headers=["Index", "x", "y"], tablefmt="pretty"))

# Calculate regression lines
mean1 = calculate_mean(data1)
mean2 = calculate_mean(data2)
std_dev1 = calculate_standard_deviation(data1)
std_dev2 = calculate_standard_deviation(data2)
correlation_coefficient = calculate_correlation_coefficient(data1, data2)
slope_y_on_x = correlation_coefficient * std_dev2 / std_dev1
intercept_y_on_x = mean2 - slope_y_on_x * mean1
slope_x_on_y = correlation_coefficient * std_dev1 / std_dev2
intercept_x_on_y = mean1 - slope_x_on_y * mean2

# Print the equation of regression line y on x
print(f"Regression line (y on x): y = {slope_y_on_x:.2f}x + {intercept_y_on_x:.2f}")

# Print the equation of regression line x on y
print(f"Regression line (x on y): x = {slope_x_on_y:.2f}y + {intercept_x_on_y:.2f}")

# Plot data and regression lines
plt.scatter(data1, data2, color='blue')
plt.plot(data1, [slope_y_on_x * x + intercept_y_on_x for x in data1], color='red', label='y on x')
plt.plot([slope_x_on_y * y + intercept_x_on_y for y in data2], data2, color='green', label='x on y')
plt.xlabel('Value1')
plt.ylabel('Value2')
plt.legend()
plt.show()
