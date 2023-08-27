# Define a function named 'print_hello' that takes a 'message' parameter and an optional 'is_lower' parameter
def print_hello(message, is_lower=False):
    # Check if the 'is_lower' parameter is True
    if is_lower:
        # Print the message in lowercase if 'is_lower' is True
        print(message.lower())
    else:
        # Print the message in uppercase if 'is_lower' is False (default)
        print(message.upper())

# Define the main function
def main():
    # Call the 'print_hello' function with the message 'Hello, Universe!'
    print_hello('Hello, Universe!')

    # Call the 'print_hello' function with the message 'Hello, Universe!' and 'is_lower' set to True
    print_hello('Hello, Universe!', True)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# HELLO, UNIVERSE!
# hello, universe!
