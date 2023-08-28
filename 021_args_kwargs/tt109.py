# Define a function 'items' that accepts keyword arguments as a dictionary-like structure
def items(**fruits):
    print(type(fruits))  # Print the type of the 'fruits' parameter (it's a dictionary)

    # Iterate through each key-value pair in the 'fruits' dictionary
    for fruit, price in fruits.items():
        print(f"{fruit} : {price}")  # Print the fruit and its price

# Define the main function
def main():
    # Call the 'items' function with keyword arguments representing fruits and their prices
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
