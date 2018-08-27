# Define the main function
def main():
    # Create a list 'books' containing book titles
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']

    # Create a tuple 'movies' containing movie titles
    movies = ('A Christmas Carol', 'The Sea Beast', 'Enchanted', 'Pinocchio', 'The Addams Family')

    # Create a range of numbers from 0 to 9 (10 exclusive)
    numbers = range(10)

    # Check if 'A Christmas Carol' is present in the 'books' list
    print('A Christmas Carol' in books)

    # Check if 'Enchanted' is present in the 'movies' tuple
    print('Enchanted' in movies)

    # Check if the number 5 is present in the 'numbers' range
    print(5 in numbers)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output:
# False
# True
# True
