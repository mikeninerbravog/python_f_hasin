# Define a function named 'main'
def main():
    # Create a list of horror books
    horror_books = ['Dracula', 'Carmilla', 'The Imago Sequence']

    # Remove and print the last book using the 'pop()' method
    removed_book = horror_books.pop()
    print(removed_book)

    # Print the updated list after removal
    print(horror_books)


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the expected output as comments
# The Imago Sequence
# ['Dracula', 'Carmilla']
