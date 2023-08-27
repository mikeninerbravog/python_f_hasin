# Define a function named 'main'
def main():
    # Use multiple assignment to assign values to variables
    # 'book' gets 'Dracula', 'author' gets 'Bram Stoker', and so on
    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

    # Use an f-string to format and print the information
    print(
        f'{book} is a novel by {author}, published in {release_year}. It has a rating of {goodreads_rating} on goodreads.')


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the formatted output as comments
# Dracula is a novel by Bram Stoker, published in 1897. It has a rating of 4.01 on goodreads.
