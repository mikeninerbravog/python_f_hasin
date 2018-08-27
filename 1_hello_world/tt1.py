# Import the 'greet' function from the 'tt_library' module
from tt_library import greet


# Define the main function
def main():
    # Call the 'greet' function from the imported module
    greet()


# Check if this script is being run as the main program

"""
if __name__ == '__main__':: This line is a common idiom in Python. It checks if the script is being run as the 
main program. The special variable __name__ holds the name of the current module. When a Python script is run, 
if it's the main program being executed, __name__ is set to '__main__'. 

main(): If the script is being run as the main program (not imported as a module), this line calls the main function, 
which, in turn, calls the greet function. 
+
"""

if __name__ == '__main__':
    # Call the 'main' function only if this script is the main program
    main()
