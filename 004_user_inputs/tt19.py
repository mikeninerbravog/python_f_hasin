def main():
    name = input('What is your name? ')
    age = input(f'How old are you {name}? ')
    current_year = input(f'What year is this again? ')

    print(f'If my calculations are right, you were born in {current_year - age}')


if __name__ == '__main__':
    main()

# What is your name? Farhan
# How old are you Farhan? 27
# What year is this again? 2023

# TypeError: unsupported operand type(s) for -: 'str' and 'str'