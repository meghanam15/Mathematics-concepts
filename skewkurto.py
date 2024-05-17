def skewness_dc(data, midpoints, frequencies):
    mean_val = sum(midpoints[i] * frequencies[i] for i in range(len(midpoints))) / sum(frequencies)
    variance = sum(((midpoints[i] - mean_val) ** 2) * frequencies[i] for i in range(len(midpoints))) / sum(frequencies)
    std_deviation = variance ** 0.5
    print("Standard deviation:", std_deviation)
    n = len(frequencies)

    # Calculate skewness
    skew = sum((midpoints[i] - mean_val) ** 3 for i in range(len(midpoints)))
    print("Summation of (xi - xmean) raised to power 3:",skew)
    skew /= (n - 1) * (std_deviation ** 3)
    return skew

def kurtosis_dc(data, midpoints, frequencies):
    mean_val = sum(midpoints[i] * frequencies[i] for i in range(len(midpoints))) / sum(frequencies)
    variance = sum(((midpoints[i] - mean_val) ** 2) * frequencies[i] for i in range(len(midpoints))) / sum(frequencies)
    std_deviation = variance ** 0.5

    n = len(frequencies)
    kurto = sum((midpoints[i] - mean_val) ** 4 for i in range(len(midpoints)))
    print("Summation of (xi - xmean) raised to power 4:", kurto)
    kurto /= (n - 1) * (std_deviation ** 4)
    return kurto


from tabulate import tabulate

def get_input():
    class_intervals = []
    frequencies = []

    num_intervals = int(input("Enter the number of class intervals: "))

    for i in range(num_intervals):
        interval = input(f"Enter class interval {i + 1} like start-end: ")
        class_intervals.append(interval)
        frequency = int(input(f"Enter frequency for class interval {i + 1}: "))
        frequencies.append(frequency)

    # Print class intervals with frequencies
    print("\nClass Intervals with Frequencies:")
    table = [["Class Intervals", "Frequency"]]
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
skew = skewness_dc(None, midpoints, frequencies)
print("Skewness:", skew)
kurto = kurtosis_dc(None, midpoints, frequencies)
print("Kurtosis:", kurto)