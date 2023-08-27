def greet(name):
    message = 'Hello, {name}!'

    def include_name():
        global message

        message = message.format(name=name)

    include_name()
    return message


def main():
    print(greet('Farhan'))


if __name__ == '__main__':
    main()

# NameError: name 'message' is not defined

"""The NameError you encountered occurs because you're trying to modify the global variable message within the 
include_name() function without first defining it as a global variable in the global scope. The line global message 
inside the include_name() function indicates that you're trying to use the global message variable, but it has not 
been defined at the global level in your code. 

To resolve this issue, you should define the message variable as a global variable before you attempt to modify it 
within the include_name() function. Here's your code with comments: """