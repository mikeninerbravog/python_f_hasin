message = 'Hello, {name}!'


def main():
    message = message.format(name='Farhan')
    print(message)


if __name__ == '__main__':
    main()

# UnboundLocalError: local variable 'message' referenced before assignment

"""By adding the line global message within the main() function, you indicate that you want to use the global message 
variable. This prevents the UnboundLocalError and allows you to modify the global variable within the function. When 
you run the script, you'll see the output "Hello, Farhan!". If you have more questions or need further assistance, 
feel free to ask! """