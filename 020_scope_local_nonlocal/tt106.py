def greet(name):
    # Create a message template with a placeholder {name}
    message = 'Hello, {name}!'

    def include_name():
        nonlocal message  # Access the 'message' variable from the outer function's scope
        message = message.format(name=name)  # Replace the placeholder with the given 'name'

    include_name()  # Call the inner function to modify the 'message'
    return message  # Return the modified message

def main():
    # Call the greet function and print the result
    print(greet('Farhan'))

if __name__ == '__main__':
    main()

# Output:
# Hello, Farhan!
