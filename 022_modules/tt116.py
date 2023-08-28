import mathstuff


def main():
    last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    print(mathstuff.natural_sum(last_number))


if __name__ == '__main__':
    main()

# up to which number would you like to calculate the sum?
# - 10  # 1+2+3+4+5+6+7+8+9+10
# 55