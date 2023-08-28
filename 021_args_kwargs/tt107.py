# Define a function 'total' that accepts a variable number of arguments
def total(*args):
    print(type(args))  # Print the type of the 'args' parameter (it's a tuple)

    t = 0  # Initialize a variable to store the total sum
    for arg in args:
        t += arg  # Add each argument to the total sum

    return t  # Return the total sum


# Define the main function
def main():
    # Call the 'total' function with multiple arguments and print the result
    print(total(1, 2, 3, 4, 5))


# Check if this script is being run as the main program
if __name__ == '__main__':
    main()

# Output:
# <class 'tuple'>
# 15

"""Breakdown: 
1. The `total` function is defined with `*args` as its parameter, which allows it to accept a variable 
number of arguments as a tuple. 

2. Inside the `total` function: - The type of the `args` parameter is printed using 
the `type()` function, showing that it's a tuple. - A variable `t` is initialized to store the total sum. - A loop 
iterates through each argument in the `args` tuple, and their values are added to the total sum `t`. - The total sum 
`t` is returned. 

3. The `main` function is defined. 

4. Inside the `main` function: - The `total` function is called 
with arguments `(1, 2, 3, 4, 5)`, and its result is printed. 

5. The `if __name__ == '__main__':` block checks if the 
script is being run directly (not imported as a module) and calls the `main` function. 

6. When you run the script, 
the output shows the type of the `args` parameter (a tuple) and the total sum of the provided arguments (15). """
