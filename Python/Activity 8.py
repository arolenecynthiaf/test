# Function to check if first and last elements are the same
def first_last_same(numbers):
    if len(numbers) == 0:
        return False
    return numbers[0] == numbers[-1]

# Get user input
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Check and display result
result = first_last_same(numbers)
print(f"First and last numbers are the same: {result}")