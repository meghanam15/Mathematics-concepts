def correlation_coefficient(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    std_dev_x = (sum((x[i] - mean_x) ** 2 for i in range(len(x))) / n) ** 0.5
    std_dev_y = (sum((y[i] - mean_y) ** 2 for i in range(len(y))) / n) ** 0.5

    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))) / n

    correlation = covariance / (std_dev_x * std_dev_y)
    return correlation


def analyze_correlation(correlation):
    if correlation > 0:
        if correlation == 1:
            return "Perfect positive correlation"
        else:
            return "Positive correlation"
    elif correlation < 0:
        if correlation == -1:
            return "Perfect negative correlation"
        else:
            return "Negative correlation"
    else:
        return "No correlation"

from tabulate import tabulate


# Input data
n = int(input("Enter the number of data points: "))

# User input for x values
x_values = input(f"Enter {n} x values (comma separated): ")
x = list(map(float, x_values.split(',')))

# User input for y values
y_values = input(f"Enter {n} y values (comma separated): ")
y = list(map(float, y_values.split(',')))

# Combine x and y into a list of lists
data = [[x[i], y[i]] for i in range(n)]

# Print the table
print(tabulate(data, headers=["X", "Y"], tablefmt="pretty"))



# Calculate correlation coefficient
correlation = correlation_coefficient(x, y)
print("Correlation coefficient:", correlation)

# Analyze correlation
correlation_type = analyze_correlation(correlation)
print("Correlation type:", correlation_type)

