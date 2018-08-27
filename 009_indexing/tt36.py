# Define the main function
def main():
    # Create a list called 'books' containing several book titles
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow',
             'And Then There Were None', 'The ABC Murders', 'The Valley of Fear']

    # Print the first book title using index 0
    print(books[0])

    # Print the second book title using index 1
    print(books[1])

    # Print the last book title using negative index -1
    print(books[-1])

    # Print the third book title using index 2
    print(books[2])

    # Print the second-to-last book title using negative index -2
    print(books[-2])


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output:
# Dracula
# Frankenstein
# The Valley of Fear
# The Omen
# The ABC Murders
