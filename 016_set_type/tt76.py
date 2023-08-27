# Define the main function
def main():
    # Create a list with duplicate values
    numbers_list = [1, 2, 3, 4, 5, 3, 2, 4]

    # Print the original list with duplicates
    print(numbers_list)  # Prints: [1, 2, 3, 4, 5, 3, 2, 4]

    # Convert the list to a set, removing duplicates
    numbers_set = set(numbers_list)

    # Print the set with duplicates removed
    print(numbers_set)  # Prints: {1, 2, 3, 4, 5}

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# [1, 2, 3, 4, 5, 3, 2, 4]
# {1, 2, 3, 4, 5}
