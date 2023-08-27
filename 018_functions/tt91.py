# Define a function named 'hello' that takes a 'message' parameter and an optional 'is_lower' parameter
def hello(message, is_lower=False):
    # Check if the 'is_lower' parameter is True
    if is_lower:
        # Return the message in lowercase if 'is_lower' is True
        return message.lower()
    else:
        # Return the message in uppercase if 'is_lower' is False (default)
        return message.upper()

# Define the main function
def main():
    # Call the 'hello' function with the message 'Hello, Universe!' and store the returned value
    uppercase_message = hello('Hello, Universe!')
    # Print the stored uppercase message
    print(uppercase_message)

    # Call the 'hello' function with the message 'Hello, Universe!' and 'is_lower' set to True,
    # then store the returned value
    lowercase_message = hello('Hello, Universe!', True)
    # Print the stored lowercase message
    print(lowercase_message)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# HELLO, UNIVERSE!
# hello, universe!
