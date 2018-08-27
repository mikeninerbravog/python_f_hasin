# Define a function named 'main'
def main():
    # Assign the value 5.0 to the variable 'float_variable'
    float_variable = 5.0

    # Assign the value 55 to the variable 'integer_variable'
    integer_variable = 55

    # Calculate the sum of 'float_variable' and 'integer_variable'
    sum_result = float_variable + integer_variable

    # Use an f-string to format and print the sum
    print(f'the sum of {float_variable} and {integer_variable} is: {sum_result}')

    # Convert the sum to an integer using the 'int' function
    # and then format and print the result
    converted_sum = int(sum_result)
    print(f'the sum of {float_variable} and {integer_variable} converted to integer is: {converted_sum}')


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the formatted output as comments
# the sum of 5.0 and 55 is: 60.0
# the sum of 5.0 and 55 converted to integer is: 60
