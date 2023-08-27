# Define the main function
def main():
    # Define a string 'string'
    string = 'Holmes was certainly not a difficult man to live with'

    # Split the 'string' into a list of words using the 'split()' method
    word_list = string.split()  # Split the string at spaces (default separator)

    # Print the resulting list of words
    print(word_list)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output: A list containing each word from the original string
