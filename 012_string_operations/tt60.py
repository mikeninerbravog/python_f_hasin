# Define the main function
def main():
    # Define a paragraph containing the text
    paragraph = '''At three in the morning... favourable specimen of the provincial criminal officer.'''

    # Define the substring to be counted
    substring = 'morning'

    # Count the number of occurrences of the 'substring' in the 'paragraph' using the 'count()' method
    count = paragraph.count(substring)

    # Print the result
    print(f'The substring "{substring}" shows up {count} times in the paragraph.')


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output: The number of occurrences of the substring "morning" in the paragraph
