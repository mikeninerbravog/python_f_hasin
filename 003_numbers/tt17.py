# Define a function named 'main'
def main():
    # Assign the value 8 to the variable 'num_1'
    num_1 = 8

    # Assign the value 2 to the variable 'num_2'
    num_2 = 2

    # Calculate the division and modulus of 'num_1' and 'num_2' using the 'divmod' function
    # The divmod function returns a tuple with the quotient and the remainder
    result = divmod(num_1, num_2)

    # Use an f-string to format and print the information
    print(f'division and modulus of {num_1} and {num_2} is: {result}')


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the formatted output as comments
# division and modulus of 8 and 2 is: (4, 0)
