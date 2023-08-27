# Define a function named 'main'
def main():
    # Assign the value 1.25 to the variable 'float_variable'
    float_variable = 1.25

    # Assign the value 55 to the variable 'integer_variable'
    integer_variable = 55

    # Convert 'float_variable' to an integer using the 'int' function
    converted_int = int(float_variable)

    # Use an f-string to format and print the conversion result
    print(f'{float_variable} converted to an integer is: {converted_int}')

    # Convert 'integer_variable' to a float using the 'float' function
    converted_float = float(integer_variable)

    # Use an f-string to format and print the conversion result
    print(f'{integer_variable} converted to a float is: {converted_float}')


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the formatted output as comments
# 1.25 converted to an integer is: 1
# 55 converted to a float is: 55.0
