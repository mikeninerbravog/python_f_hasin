# Define a function named 'natural_sum' that calculates the sum of natural numbers up to 'last_number'
def natural_sum(last_number):
    # Check if 'last_number' is less than 1
    if last_number < 1:
        # Return 'last_number' as it is (could be a negative value)
        return last_number

    # Initialize a variable 'total' to keep track of the sum
    total = 0
    # Iterate through numbers from 1 to 'last_number'
    for number in range(1, last_number + 1):
        # Add the current 'number' to the sum 'total'
        total += number
    # Return the final sum 'total'
    return total


# Define the main function
def main():
    # Ask the user for input: the last number up to which to calculate the sum
    last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    # Call the 'natural_sum' function with 'last_number' and print the returned sum
    print(natural_sum(last_number))


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# up to which number would you like to calculate the sum?
# - 10
# 55
