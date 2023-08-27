# Define the main function
def main():
    # Define a string 'book_name'
    book_name = 'moriarty'

    # Print the value of 'book_name'
    print(book_name)

    # Check if 'book_name' is in uppercase using the 'isupper()' method
    print(f'Is {book_name} in upper case? {book_name.isupper()}')

    # Check if 'book_name' is in lowercase using the 'islower()' method
    print(f'Is {book_name} in lower case? {book_name.islower()}')

    # Define another string 'another_book_name'
    another_book_name = 'DRACULA'

    # Print the value of 'another_book_name'
    print(another_book_name)

    # Check if 'another_book_name' is in lowercase using the 'islower()' method
    print(f'Is {another_book_name} in upper case? {another_book_name.islower()}')

    # Check if 'another_book_name' is in uppercase using the 'isupper()' method
    print(f'Is {another_book_name} in lower case? {another_book_name.isupper()}')

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output:
# moriarty
# Is moriarty in upper case? False
# Is moriarty in lower case? True
# DRACULA
# Is DRACULA in upper case? True
# Is DRACULA in lower case? False
