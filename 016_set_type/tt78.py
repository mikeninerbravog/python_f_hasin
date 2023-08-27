# Define the main function
def main():
    # Create a set with initial values
    numbers = {1, 2, 3, 4, 5}

    # Remove the value 3 from the set using the 'discard' method
    numbers.discard(3)

    # Print the modified set
    print(numbers)  # Prints: {1, 2, 4, 5}

    # Clear all elements from the set using the 'clear' method
    numbers.clear()

    # Print the cleared set (which will be an empty set)
    print(numbers)  # Prints: set()

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# {1, 2, 4, 5}
# set()
