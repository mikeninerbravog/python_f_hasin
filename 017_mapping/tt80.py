# Define the main function
def main():
    # Create a dictionary of programming books with titles as keys and prices as values
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    # Define book titles to look up
    cpl = 'C Programming Language'
    algo = 'Introduction to Algorithms'

    # Print the prices of the specified books using 'get' and dictionary indexing
    print(f"The price of {cpl} is ${programming_books.get(cpl)}")
    print(f"The price of {algo} is ${programming_books[algo]}")

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# The price of C Programming Language is $35
# The price of Introduction to Algorithms is $100
