# Define the main function
def main():
    # Create a list 'books' containing book titles
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']

    # Create another list 'more_books' containing additional book titles
    more_books = ['And Then There Were None', 'The ABC Murders', 'The Valley of Fear', 'The Hound of the Baskervilles',
                  'The Chestnut Man']

    # Concatenate the 'books' and 'more_books' lists using the '+' operator
    combined_books = books + more_books

    # Print the combined list of books
    print(combined_books)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output: A combined list containing all book titles from 'books' and 'more_books'
