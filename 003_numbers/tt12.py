# Define a function named 'main'
def main():
    # Assign the value 15 to the variable 'num_1'
    num_1 = 15

    # Assign the value 12 to the variable 'num_2'
    num_2 = 12

    # Calculate the remainder of 'num_1' divided by 'num_2' using the modulus operator %
    remainder = num_1 % num_2

    # Use an f-string to format and print the remainder
    print(f'remainder of num_1 / num_2 is: {remainder}')


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the formatted output as a comment
# remainder of num_1 / num_2 is: 3
