# Define the main function
def main():
    # Use a 'for' loop to iterate through numbers from 1 to 5 (exclusive)
    for x in range(1, 6):
        # Print a new line for formatting
        print()

        # Use another 'for' loop to iterate through numbers from 1 to 10 (exclusive)
        for y in range(1, 11):
            # Print the multiplication expression using f-string formatting
            print(f"{x} x {y} = {x * y}")


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output: Multiplication table for numbers 1 to 5, from 1 to 10
# Each section of the output is separated by empty lines for better readability
