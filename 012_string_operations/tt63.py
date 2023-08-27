# Define the main function
def main():
    # Define a list 'word_list'
    word_list = ['Holmes', 'was', 'certainly', 'not', 'a', 'difficult', 'man', 'to', 'live', 'with']

    # Initialize an empty string 'string'
    string = ''

    # Join the elements of 'word_list' with an empty string and assign the result to 'string'
    string = string.join(word_list)

    # Print the concatenated 'string'
    print(string)

    # Define another list 'word_list'
    word_list = ['Holmes ', 'was ', 'certainly ', 'not ', 'a ', 'difficult ', 'man ', 'to ', 'live ', 'with']

    # Reset the 'string' to an empty string
    string = ''

    # Join the elements of 'word_list' with an empty string and assign the result to 'string'
    string = string.join(word_list)

    # Print the concatenated 'string'
    print(string)


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output:
# Holmeswascertainlynotadifficultmantolivewith
# Holmes was certainly not a difficult man to live with
