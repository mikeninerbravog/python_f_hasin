# Define the main function
def main():
    # Get user input for shield and sword levels
    shield = int(input('what is your shield level? '))
    sword = int(input('what is your sword level? '))

    # Check if shield level is 45 or higher AND sword level is 48 or higher
    if shield >= 45 and sword >= 48:
        print('you shall pass!')
    else:
        print('you shall not pass!')

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example interaction:
# what is your shield level? 42
# what is your sword level? 52
# Output: you shall not pass!
