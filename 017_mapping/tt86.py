# Define the main function
def main():
    # Create a dictionary of programming books with titles as keys and prices as values
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    # Iterate through the items (key-value pairs) of the dictionary and print each item
    for item in programming_books.items():
        print(item)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# ('C Programming Language', 35)
# ('Introduction to Algorithms', 100)
# ('Clean Code: A Handbook of Agile Software Craftsmanship', 50)
