# Define the main function
def main():
    # Define a string 'book_name'
    book_name = 'hearts in atlantis'

    # Check if the original 'book_name' is in title case using the 'istitle()' method
    print(f'Is "{book_name}" in title case? {book_name.istitle()}')

    # Convert 'book_name' to title case using the 'title()' method and then check if it's in title case
    print(f'Is "{book_name.title()}" in title case? {book_name.title().istitle()}')


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output: Checking whether the original and title-cased versions of 'book_name' are in title case
