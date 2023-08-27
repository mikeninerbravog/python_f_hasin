def greet(name):
    message = 'Hello, {name}!'

    def include_name():
        message = message.format(name=name)

    include_name()
    return message


def main():
    print(greet('Farhan'))


if __name__ == '__main__':
    main()

# UnboundLocalError: local variable 'message' referenced before assignment

"""You encountered an UnboundLocalError because you're trying to modify the message variable 
inside the include_name() function before it has been assigned a value in the local scope of that function. 
In Python, when you assign a value to a variable within a function, Python treats it as a local variable by default. 

To fix this issue, you can use the nonlocal keyword inside the include_name() function to indicate that you want to 
modify the message variable from the outer function's scope. Here's your code with comments: """