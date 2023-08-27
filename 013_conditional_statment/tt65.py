# Define the main function
def main():
    # Ask the user for input: the year to be checked for leapness
    year = int(input('which year would you like to check?\n- '))

    # Check if the given year is divisible by 400 and also divisible by 100
    if year % 400 == 0 and year % 100 == 0:
        print(f"{year} is leap year.")
    # Check if the given year is divisible by 4 and not divisible by 100
    elif year % 4 == 0 and year % 100 != 0:
        print(f"{year} is leap year.")
    # If none of the above conditions are met, it's not a leap year
    else:
        print(f"{year} is not leap year.")

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()
