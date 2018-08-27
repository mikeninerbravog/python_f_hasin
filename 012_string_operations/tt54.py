# Import the 'capwords' function from the 'string' module
from string import capwords

# Define the main function
def main():
    # Create a string 'address' containing address components
    address = 'house 42, road 02, wonderland'

    # Use the 'capwords' function to capitalize words in the 'address' string, using ', ' as the separator
    formatted_address = capwords(address, ', ')

    # Print the formatted address
    print(formatted_address)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output: The address with capitalized words after each comma and space
