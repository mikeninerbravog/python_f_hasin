# Define a function named 'main'
def main():
    # Assign the value 15 to the variable 'num_1'
    num_1 = 15

    # Assign the value 12 to the variable 'num_2'
    num_2 = 12

    # Calculate the sum of 'num_1' and 'num_2' using the addition operator '+'
    sum_result = num_1 + num_2

    # Calculate the difference between 'num_1' and 'num_2' using the subtraction operator '-'
    difference = num_1 - num_2

    # Use f-strings to format and print the sum and difference
    print(f'sum of num_1 and num_2 is: {sum_result}')
    print(f'difference of num_1 and num_2 is: {difference}')


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the formatted output as comments
# sum of num_1 and num_2 is: 27
# difference of num_1 and num_2 is: 3
