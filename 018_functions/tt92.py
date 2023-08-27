# Define a function named 'total' that takes a list of 'numbers' as a parameter
def total(numbers):
    # Initialize a variable 's' to keep track of the sum
    s = 0
    # Iterate through each 'number' in the 'numbers' list
    for number in numbers:
        # Add the current 'number' to the sum 's'
        s += number
    # Return the final sum 's'
    return s

# Define the main function
def main():
    # Call the 'total' function with a list of numbers and print the returned sum
    print(total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# 55
