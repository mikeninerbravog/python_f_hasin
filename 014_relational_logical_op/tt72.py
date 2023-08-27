# Define the main function
def main():
    # Set the age and Van Helsing status
    age = 800_000  # Age in years
    is_van_helsing = True  # Van Helsing status (True or False)

    # Check if the player is both over 500,000 years old and not Van Helsing
    if age > 500_000 and not is_van_helsing:
        print('you shall pass!')
    else:
        print('you shall not pass!')

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output: you shall not pass!
