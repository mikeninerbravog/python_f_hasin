def main():
    temperature_in_celsius = input('What is the temperature in celsius? ')

    temperature_in_fahrenheit = (float(temperature_in_celsius) * 1.8) + 32

    print(f'{temperature_in_celsius} degree celsius is equivalent to {temperature_in_fahrenheit} degree fahrenheit.')


if __name__ == '__main__':
    main()

# What is the temperature in celsius? 32
# 32 degree celsius is equivalent to 89.6 degree fahrenheit.