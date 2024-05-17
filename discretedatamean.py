def calculate_mean(data):
    return sum(data) / len(data)


def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]


def calculate_mode(data):
    data_set = list(set(data))
    max_count = 0
    modes = []
    for num in data_set:
        count = data.count(num)
        if count > max_count:
            max_count = count
            modes = [num]
        elif count == max_count:
            modes.append(num)
    return modes

def main():
    data = input("Enter a list of numbers separated by spaces: ").split()
    data = [int(x) for x in data]
    print("List of numbers:", data)
    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)

    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)

main()
