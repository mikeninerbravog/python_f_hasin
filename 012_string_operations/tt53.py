# Import the 'capwords' function from the 'string' module
from string import capwords


# Define the main function
def main():
    # Define a string 'book_name'
    book_name = "alice's adventures in wonderland"

    # Use the 'capwords' function to capitalize the words in 'book_name'
    capitalized_name = capwords(book_name)

    # Print the capitalized name
    print(capitalized_name)


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output: The string 'book_name' with each word capitalized
