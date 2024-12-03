def process_input_file(file_path):
    # Initialize the lists
    L = []
    R = []
    
    # Open and read the input file
    with open(file_path, "r") as file:
        for line in file:
            # Split each line into two integers and add them to L and R
            num1, num2 = map(int, line.strip().split())
            L.append(num1)
            R.append(num2)
    
    return L, R

# Example usage
file_path = "./input.txt"  # Replace with the path to your input file
L, R = process_input_file(file_path)
print("List L:", L)
print("List R:", R)
