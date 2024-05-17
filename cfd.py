from tabulate import tabulate
def mean_cfd(class_intervals, frequencies):
    class_midpoints = [(lower + upper) / 2 for lower, upper in class_intervals]
    total_frequency = sum(frequencies)
    weighted_sum = sum(midpoint * frequency for midpoint, frequency in zip(class_midpoints, frequencies))
    mean = weighted_sum / total_frequency
    return mean

def median_cfd(class_intervals, frequencies):
    total_frequency = sum(frequencies)
    cumulative_frequency = 0

    for i, (lower_bound, upper_bound) in enumerate(class_intervals):
        frequency = frequencies[i]
        cumulative_frequency += frequency
        if cumulative_frequency >= total_frequency / 2:
            L = lower_bound
            h = upper_bound - lower_bound
            f = frequency
            c = cumulative_frequency - frequency
            median = L + (h/f) * ((total_frequency / 2) - c)
            print(c)
            return median

def mode_cfd(class_intervals, frequencies):
    max_freq_index = frequencies.index(max(frequencies))
    L,U = class_intervals[max_freq_index]
    h = U - L
    f1 = frequencies[max_freq_index]
    if max_freq_index > 0:
        f0 = frequencies[max_freq_index - 1]
    else:
        f0 = 0
    if max_freq_index < len(frequencies) - 1:
        f2 = frequencies[max_freq_index + 1]
    else:
        f2 = 0

    mode = L + (h * (f1-f0)) / (2 * f1 - f0 - f2)

    return mode

def get_input():
    class_intervals = []
    frequencies = []
    num_intervals = int(input("Enter the number of intervals: "))

    for _ in range(num_intervals):
        lower_bound , upper_bound = map(int, input("Enter class interval(lower_bound upper_bound): ").split())
        frequency = int(input("Enter frequency: "))
        class_intervals.append((lower_bound, upper_bound))
        frequencies.append(frequency)

    print("\nClass Intervals with Frequencies:")
    table = [["Interval", "Frequency"]]
    for interval, frequency in zip(class_intervals, frequencies):
        lower_bound, upper_bound = interval
        table.append([f"{lower_bound}-{upper_bound}", frequency])

    print(tabulate(table, headers="firstrow", tablefmt='pretty'))

    return class_intervals, frequencies

class_intervals, frequencies = get_input()
median = median_cfd(class_intervals, frequencies)
mode = mode_cfd(class_intervals, frequencies)
mean = mean_cfd(class_intervals, frequencies)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)