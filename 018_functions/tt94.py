# Define a recursive function named 'recursive_natural_sum' that calculates the sum of natural numbers up to 'last_number'
def recursive_natural_sum(last_number):
    # Check if 'last_number' is less than 1
    if last_number < 1:
        # Return 'last_number' as it is (could be a negative value)
        return last_number

    # Return the sum of 'last_number' and the result of the recursive call to 'recursive_natural_sum'
    return last_number + recursive_natural_sum(last_number - 1)


# Define the main function
def main():
    # Ask the user for input: the last number up to which to calculate the sum
    last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    # Call the 'recursive_natural_sum' function with 'last_number' and print the returned sum
    print(recursive_natural_sum(last_number))


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# up to which number would you like to calculate the sum?
# - 10
# 55
