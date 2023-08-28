# Example 3: Find Maximum

# Define a function that finds the maximum value among a variable number of arguments.
def find_maximum(*values):
    maximum = max(values)  # Using the built-in max() function to find the maximum value.
    return maximum  # Return the maximum value found.


# Call the find_maximum() function with a sequence of values as arguments.
result = find_maximum(5, 9, 2, 12, 7)

# Print the result of finding the maximum value.
print(result)  # Output: 12
