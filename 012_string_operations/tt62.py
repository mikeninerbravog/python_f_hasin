# Define the main function
def main():
    # Define a string 'string'
    string = 'Holmes,was,certainly,not,a,difficult,man,to,live,with'

    # Split the 'string' using ',' as the delimiter and limit the split to 5 parts
    word_list = string.split(',', 5)

    # Print the resulting list 'word_list'
    print(word_list)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output:
# ['Holmes', 'was', 'certainly', 'not', 'a', 'difficult,man,to,live,with']
