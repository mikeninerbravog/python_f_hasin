# Define a function named 'main'
def main():
    # Assign values to variables
    book = 'Dracula'
    author = 'Bram Stoker'
    release_year = 1897
    goodreads_rating = 4.01

    # Convert integer values to strings and concatenate them with other strings
    # Use the '+' operator for string concatenation
    output = book + ' is a novel by ' + author + ', published in ' + str(release_year) + '. It has a rating of ' + str(
        goodreads_rating) + ' on goodreads.'

    # Print the final concatenated string
    print(output)


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the output as a comment
# Dracula is a novel by Bram Stoker, published in 1897. It has a rating of 4.01 on goodreads.
