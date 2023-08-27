# Define the main function
def main():
    # Create a list of numbers
    numbers = [1, 2, 5, 4, 7, 88, 12, 15, 55, 77, 95]

    # Use the 'filter' function with a lambda function to filter even numbers
    even_numbers = filter(lambda number: True if number % 2 == 0 else False, numbers)

    # Convert the result of the 'filter' function into a list and print it
    print(list(even_numbers))


# Check if this script is the main entry point
if __name__ == '__main__':
    # Call the 'main' function if this script is being run directly
    main()

# Example output:
# [2, 4, 88, 12]

"""
1. The `main` function is defined. This function will be the entry point for the program.

2. A list named `numbers` is created, containing a sequence of numbers.

3. The `filter` function is used with a lambda function as its first argument. The lambda function takes a `number` 
as input and returns `True` if the number is even (i.e., divisible by 2), otherwise it returns `False`. 

4. The result of the `filter` function is an iterable, which contains the even numbers from the `numbers` list 
according to the condition defined in the lambda function. 

5. The result of the `filter` function is then converted to a list using the `list()` function.

6. The resulting list of even numbers is printed using the `print()` function.

7. The block under `if __name__ == '__main__':` checks whether the current script is being run directly (not imported 
as a module). If this condition is true, the `main` function is called. 

8. When you run the script, it filters the even numbers from the `numbers` list using the lambda function and prints 
the filtered even numbers as a list. 

Example output: ``` [2, 4, 88, 12] ``` In summary, this script demonstrates how to use the `filter` function along 
with a lambda function to filter even numbers from a list and then print the filtered numbers. 

"""
