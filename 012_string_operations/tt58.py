# Define the main function
def main():
    # Define a string 'book_name'
    book_name = 'DRACULA'

    # Convert 'book_name' to lowercase using the 'casefold()' method
    lowercase_book_name = book_name.casefold()

    # Print the lowercase version of 'book_name'
    print(lowercase_book_name)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output: The lowercase version of the 'book_name' string
