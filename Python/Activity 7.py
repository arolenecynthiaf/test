# Get user input for the list
user_input = input("Enter numbers separated by spaces: ")

# Convert input string to a list of integers
numbers = list(map(int, user_input.split()))

# Calculate the sum
total = sum(numbers)

# Display the result
print(f"List: {numbers}")
print(f"Sum: {total}")