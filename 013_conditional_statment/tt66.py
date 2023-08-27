# Define the main function
def main():
    # Prompt the user to input a number to check for primality
    number = int(input('what number would you like to check?\n- '))

    # Initialize a flag to indicate whether the number is not prime
    is_not_prime = False

    # Check special cases for numbers 1 and greater than 1
    if number == 1:
        print(f"{number} is not a prime number.")
    elif number > 1:
        # Iterate through potential divisors from 2 up to (number - 1)
        for n in range(2, number):
            # If 'number' is divisible by 'n', it's not a prime number
            if (number % n) == 0:
                is_not_prime = True
                break

        # Check the flag to determine if the number is prime or not
        if is_not_prime:
            print(f"{number} is not a prime number.")
        else:
            print(f"{number} is a prime number.")


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example usage:
# what number would you like to check?
# - 10
# 10 is not a prime number.
