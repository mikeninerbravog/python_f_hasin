# Declare a global variable 'message' with a placeholder for the name
message = 'Hello, {name}!'


# Define the main function
def main():
    # Create an empty string named 'message'
    message = str()

    # Format the 'message' string with the name 'Farhan'
    message = message.format(name='Farhan')
    print(message)


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# Hello, Farhan!
