# Define a function named 'check_even' that returns True if a number is even, and False otherwise
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Define the main function
def main():
    # Create a list of numbers
    numbers = [1, 2, 5, 4, 7, 88, 12, 15, 55, 77, 95]

    # Use the 'filter' function with 'check_even' and 'numbers' to get even numbers
    even_numbers = filter(check_even, numbers)

    # Convert the result of the 'filter' function into a list and print it
    print(list(even_numbers))

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# [2, 4, 88, 12]
