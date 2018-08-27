# Define the main function
def main():
    # Create a list called 'random_numbers' containing various integers
    random_numbers = [6, 1, 3, 8, 0, 9, 12, 3, 4, 0, 54, 8, 100, 55, 60, 70, 85]

    # Use a 'for' loop to iterate over each 'number' in the 'random_numbers' list
    for number in random_numbers:
        # Multiply the current 'number' by 2 and print the result
        print(number * 2)

# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# The expected output: Each number in the 'random_numbers' list multiplied by 2, printed on separate lines
# 12
# 2
# 6
# 16
# 0
# 18
# 24
# 6
# 8
# 0
# 108
# 16
# 200
# 110
# 120
# 140
# 170
