# Define the main function
def main():
    # Create an empty dictionary 'numbers' and print its type
    numbers = {}  # This creates an empty dictionary
    print(type(numbers))  # Prints: <class 'dict'>

    # Create an empty set 'numbers' and print its type
    numbers = set()  # This creates an empty set
    print(type(numbers))  # Prints: <class 'set'>

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# <class 'dict'>
# <class 'set'>
