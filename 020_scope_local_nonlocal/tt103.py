# Declare a global variable 'message' with a placeholder for the name
message = 'Hello, {name}!'

# Define the main function
def main():
    # Use the global 'message' variable and format it with the name 'Farhan'
    global message
    message = message.format(name='Farhan')
    print(message)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# Hello, Farhan!
