# Define a function named 'main'
def main():
    # Create a range of numbers using the 'range()' function with start=1, stop=10, and step=2
    a_range = range(1, 10, 2)

    # Print the 'a_range' object (a range of numbers)
    print(a_range)

    # Convert the 'a_range' object to a list using the 'list()' function
    list_a_range = list(a_range)

    # Print the 'list_a_range' (a list of numbers)
    print(list_a_range)

    # Convert the 'a_range' object to a tuple using the 'tuple()' function
    tuple_a_range = tuple(a_range)

    # Print the 'tuple_a_range' (a tuple of numbers)
    print(tuple_a_range)


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the expected outputs as comments
# range(1, 10, 2)
# [1, 3, 5, 7, 9]
# (1, 3, 5, 7, 9)
