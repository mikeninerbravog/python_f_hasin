# Define a function named 'main'
def main():
    # Assign the value 2 to the variable 'x'
    x = 2

    # Assign the value 3 to the variable 'y'
    y = 3

    # Calculate 2 raised to the power of 3 using the 'pow' function
    result_1 = pow(2, 3)

    # Calculate 2 raised to the power of 3 using the exponentiation operator **
    result_2 = 2 ** 3

    # Use an f-string to format and print the first result
    print(f'{2} to the power of {3} is: {result_1}')

    # Use an f-string to format and print the second result
    print(f'{2} to the power of {3} is: {result_2}')


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the formatted output as comments
# 2 to the power of 3 is: 8
# 2 to the power of 3 is: 8
