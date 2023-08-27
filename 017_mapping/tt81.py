# Define the main function
def main():
    # Create a dictionary of programming books with titles as keys and prices as values
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    # Specify the key for the book to modify
    key = 'C Programming Language'

    # Modify the price of the specified book
    programming_books[key] = 45

    # Add a new book to the dictionary with its price
    programming_books['The Pragmatic Programmer'] = 32

    # Print the modified dictionary of programming books
    print(programming_books)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# {'C Programming Language': 45, 'Introduction to Algorithms': 100,
# 'Clean Code: A Handbook of Agile Software Craftsmanship': 50, 'The Pragmatic Programmer': 32}
