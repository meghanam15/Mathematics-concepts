from tabulate import tabulate

def get_input():
    data = []
    frequency = []
    num_values = int(input("Enter the number of values: "))

    for i in range(num_values):
        value = float(input("Enter the value: "))
        freq = float(input("Enter the frequency: "))
        data.append(value)
        frequency.append(freq)
    return data, frequency

def create_table(data, frequency):
    table = [["Value", "Frequency"]]
    for d, f in zip(data, frequency):
        table.append([d, f])
    return table

data, frequency = get_input()
table_data = create_table(data, frequency)
print(tabulate(table_data, headers="firstrow", tablefmt="pretty"))


def mean_discrete_frequency(data,frequency):
    total = 0
    frequency_sum = sum(frequency)
    for i in range(len(data)):
        total += data[i] * frequency[i]

    return total / frequency_sum

mean = mean_discrete_frequency(data,frequency)
print("Mean:",mean)

def median_discrete_frequency(data, frequency):
    sorted_data = sorted(zip(data, frequency))
    total_frequency = sum(frequency)

    cumulative_frequency = 0
    for value,freq in sorted_data:
        cumulative_frequency += freq
        if cumulative_frequency >= total_frequency / 2:
            return value

median = median_discrete_frequency(data,frequency)
print("Median:",median)

def mode_discrete_frequency(data,frequency):
    max_frequency = max(frequency)
    mode = [(data[i],frequency[i]) for i in range(len(data)) if frequency[i] == max_frequency]
    return mode

mode = mode_discrete_frequency(data, frequency)
print("Mode(s) and their frequencies:", mode)