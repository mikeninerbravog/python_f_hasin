# Define the main function
def main():
    # Set the age and legal death status
    age = 10_000  # Age in years
    is_legally_dead = True  # Legal death status (True or False)

    # Check if the player is either legally dead or more than 500,000 years old
    if is_legally_dead or age > 500_000:
        print('you shall pass!')
    else:
        print('you shall not pass!')

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output: you shall pass!
