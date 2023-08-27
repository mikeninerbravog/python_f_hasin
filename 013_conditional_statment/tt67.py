# Define the main function
def main():
    # Get user input for the number to be checked
    number = int(input('what number would you like to check?\n- '))

    # Check if the number is equal to 1
    if number == 1:
        print(f"{number} is not a prime number.")
    # Check if the number is greater than 1
    elif number > 1:
        # Use a loop to check divisibility from 2 to (number - 1)
        for n in range(2, number):
            # If the number is divisible by 'n', it's not a prime number
            if (number % n) == 0:
                print(f"{number} is not a prime number.")
                break
        # If the loop completes without a break, the number is a prime number
        else:
            print(f"{number} is a prime number.")


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example interaction:
# what number would you like to check?
# - 5
# Output: 5 is a prime number.
