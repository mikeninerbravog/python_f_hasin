# Define a function named 'main'
def main():
    # Assign values to variables
    book = 'Dracula'
    author = 'Bram Stoker'
    release_year = 1897
    goodreads_rating = 4.01

    # Use f-strings to format and print the output
    print(f'{book} is a novel by {author}, published in {release_year}.'
          f' It has a rating of {goodreads_rating} on goodreads.')


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Call the 'main' function if this script is the main program
    main()

# Print the formatted output as a comment
# Dracula is a novel by Bram Stoker, published in 1897. It has a rating of 4.01 on goodreads.
