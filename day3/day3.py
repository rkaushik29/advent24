import re

def read_file(filename):
    input_string = ''
    with open(filename, 'r') as file:
        for line in file:
            input_string += line
    
    return input_string


def find_muls(memory):
    mul_enabled = True
    total = 0
    instruction_pattern = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")

    for match in instruction_pattern.finditer(memory):
        instruction = match.group(0)

        if instruction == "do()":
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False
        elif instruction.startswith("mul(") and mul_enabled:
            x, y = map(int, re.findall(r"\d+", instruction))
            total += x * y

    return total

file = './input.txt'
input = read_file(file)
print(find_muls(input))