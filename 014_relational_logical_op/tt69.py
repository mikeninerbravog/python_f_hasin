# Define the main function
def main():
    # Get user input for shield, sword, and armor levels
    shield = int(input('what is your shield level? '))
    sword = int(input('what is your sword level? '))
    armor = int(input('what is your armor level? '))

    # Check if shield level is 45 or higher, sword level is 48 or higher, and armor level is 25 or higher
    if shield >= 45 and sword >= 48 and armor >= 25:
        print('you shall pass!')
    else:
        print('you shall not pass!')


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example interaction:
# what is your shield level? 45
# what is your sword level? 50
# what is your armor level? 10
# Output: you shall not pass!
