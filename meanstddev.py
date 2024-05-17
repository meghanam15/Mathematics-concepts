def mean_dc(data, midpoints,frequencies):
    mean_val = sum(midpoints[i] * frequencies[i] for i in range(len(midpoints))) / sum(frequencies)
    mean_deviation = sum(abs(midpoints[i] - mean_val) * frequencies[i] for i in range(len(midpoints))) / sum(frequencies)
    return mean_deviation,mean_val

def std_dc(data, midpoints, frequencies):
    mean_val = sum(midpoints[i] * frequencies[i] for i in range(len(midpoints))) / sum(frequencies)
    variance = sum((midpoints[i] - mean_val) ** 2 * frequencies[i] for i in range(len(midpoints))) / sum(frequencies)
    std_deviation = variance ** 0.5
    return std_deviation,variance

from tabulate import tabulate

def get_input():
    class_intervals = []
    frequencies = []

    num_intervals = int(input("Enter the number of class intervals: "))

    for i in range(num_intervals):
        interval = input(f"Enter class interval {i+1} like start-end: ")
        class_intervals.append(interval)
        frequency = int(input(f"Enter frequency for class interval {i+1}: "))
        frequencies.append(frequency)

    # Print class intervals with frequencies
    print("\nClass Intervals with Frequencies:")
    table = [["Class Intervals", "Frequencies"]]
    for interval, frequency in zip(class_intervals, frequencies):
        table.append([interval, frequency])

    print(tabulate(table, headers="firstrow", tablefmt="pretty"))

    return class_intervals, frequencies


def find_midpoints(class_intervals):
    midpoints = []
    for interval in class_intervals:
        start, end = map(int, interval.split('-'))
        midpoint = (start+end) / 2
        midpoints.append(midpoint)
    return midpoints

class_intervals, frequencies = get_input()
midpoints = find_midpoints(class_intervals)

print("Midpoints:", midpoints)
print("Frequencies:", frequencies)

mean_deviation, mean_val = mean_dc(None, midpoints, frequencies)
print("Mean value:", mean_val)
print("Mean deviation:", mean_deviation)


std_deviation, variance = std_dc(None, midpoints, frequencies)
print("Standard deviation:", std_deviation)
print("Variance:", variance)

print("Analysing dispersion")
if std_deviation < mean_val:
    print("The data has low dispersion")
elif std_deviation == mean_val:
    print("The data has uniform dispersion")
else:
    print("the data has high dispersion")
if mean_deviation < std_deviation:
    print("Mean deviation indicates lower dispersion compared to standard deviation.")
elif mean_deviation == std_deviation:
    print("Mean deviation and standard deviation suggest similar dispersion.")
else:
    print("Mean deviation indicates higher dispersion compared to standard deviation.")