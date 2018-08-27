# Define a function named 'main'
def main():
    # Create a range of numbers using the 'range()' function with stop=10
    a_range = range(10)

    # Print the 'a_range' object (a range of numbers from 0 to 9)
    print(a_range)

    # Convert the 'a_range' object to a list using the 'list()' function
    list_a_range = list(a_range)

    # Print the 'list_a_range' (a list of numbers)
    print(list_a_range)


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the expected outputs as comments
# range(0, 10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
