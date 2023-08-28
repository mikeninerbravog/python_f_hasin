# Example 1: Sum of Numbers

# Define a function that calculates the sum of any number of arguments.
def calculate_sum(*numbers):
    total = sum(numbers)  # Using the built-in sum() function to add up the numbers.
    return total  # Return the calculated sum.

# Call the calculate_sum() function with a sequence of numbers as arguments.
result = calculate_sum(1, 2, 3, 4, 5)

# Print the result of the calculation.
print(result)  # Output: 15
