# Define the main function
def main():
    # Get input from the user and convert it to an integer
    number = int(input('What number would you like to check?\n- '))

    # Check if the number is even by using the modulo (%) operator
    if number % 2 == 0:
        # Print a message if the number is even
        print(f"{number} is even.")
    else:
        # Print a message if the number is odd
        print(f"{number} is odd.")

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output:
# A user prompt: "What number would you like to check?"
# User input: 10
# Output: "10 is even."
