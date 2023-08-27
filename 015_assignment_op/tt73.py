# Define the main function
def main():
    # Get user input for the starting and ending numbers
    start = int(input('which number do you want to start from?\n- '))
    end = int(input('which number do you want to stop at?\n- '))

    # Initialize a variable 'total' to store the sum of numbers
    total = 0

    # Use a loop to iterate through the numbers from 'start' to 'end' (inclusive)
    for number in range(start, end + 1):
        total += number  # Add the current number to the 'total' sum

    # Print the sum of the numbers in the specified range
    print(f"the sum of the numbers between {start} and {end} is: {total}")

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example interaction:
# which number do you want to start from?
# - 1
# which number do you want to stop at?
# - 10
# Output: the sum of the numbers between 1 and 10 is: 55
