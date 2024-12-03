def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(num) for num in line.strip().split()]
            numbers.append(row)
    return numbers

def is_monotonic(level):
    increasing = all(level[i] < level[i + 1] for i in range(len(level) - 1))
    decreasing = all(level[i] > level[i + 1] for i in range(len(level) - 1))
    return increasing or decreasing

def valid_differences(level):
    return all(1 <= abs(level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1))

def check_safety_with_dampener(level):
    if is_monotonic(level) and valid_differences(level):
        return True

    for i in range(len(level)):
        new_level = level[:i] + level[i+1:]  # Remove the i-th level
        if is_monotonic(new_level) and valid_differences(new_level):
            return True

    return False

def damped_safe_reactors(numbers):
    count = 0
    for report in numbers:
        if check_safety_with_dampener(report):
            count += 1
    print(f"Number of safe reports: {count}")
    return count

# Example usage
numbers = read_numbers_from_file('./input.txt')
damped_safe_reactors(numbers)
