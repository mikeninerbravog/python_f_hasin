# Define the main function
def main():
    # Create a set with initial values
    numbers = {1, 2, 3, 4, 5}

    # Add the value 500 to the set using the 'add' method
    numbers.add(500)

    # Print the modified set
    print(numbers)  # Prints: {1, 2, 3, 4, 5, 500}

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output: {1, 2, 3, 4, 5, 500}
