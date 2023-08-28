# Define a function 'items' that accepts keyword arguments as a dictionary-like structure
def items(**kwargs):
    print(type(kwargs))  # Print the type of the 'kwargs' parameter (it's a dictionary)

    # Iterate through each key-value pair in the 'kwargs' dictionary
    for key, value in kwargs.items():
        print(f"{key} : {value}")  # Print the key and value

# Define the main function
def main():
    # Call the 'items' function with keyword arguments and print the results
    items(
        Apple=10,
        Orange=8,
        Grape=35
    )

# Check if this script is being run as the main program
if __name__ == '__main__':
    main()

# Output:
# <class 'dict'>
# Apple : 10
# Orange : 8
# Grape : 35

"""
1. The `items` function is defined with `**kwargs` as its parameter, which allows it to accept keyword arguments 
as a dictionary-like structure. 

2. Inside the `items` function: - The type of the `kwargs` parameter is printed using the `type()` function, 
showing that it's a dictionary. - A loop iterates through each key-value pair in the `kwargs` dictionary. - For each 
key-value pair, it prints the key and its corresponding value. 

3. The `main` function is defined. 

4. Inside the `main` function: - The `items` function is called with keyword arguments (Apple, Orange, 
and Grape) and their respective values, creating a dictionary-like structure. 

5. The `if __name__ == '__main__':`block checks if the script is being run directly (not imported as a module) and 
calls the `main` function. 

6. When you run the script, the output shows the type of the `kwargs` parameter (a dictionary) and the key-value pairs 
provided as keyword arguments. """