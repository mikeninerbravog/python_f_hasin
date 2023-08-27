# Define the main function
def main():
    # Create a dictionary of programming books with titles as keys and prices as values
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    # Remove and return a random key-value pair from the dictionary using 'popitem'
    print(programming_books.popitem())  # Prints: ('Clean Code: A Handbook of Agile Software Craftsmanship', 50)

    # Specify the key for the book to remove and return its value using 'pop'
    key = 'C Programming Language'
    print(programming_books.pop(key))  # Prints: 35

    # Print the modified dictionary after the removals
    print(programming_books)  # Prints: {'Introduction to Algorithms': 100}

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# ('Clean Code: A Handbook of Agile Software Craftsmanship', 50)
# 35
# {'Introduction to Algorithms': 100}
