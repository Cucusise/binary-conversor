while True:
    print('Choose the value you want to convert:')
    print('|1. -----Binary -----> Decimal -----|')
    print('|2. -----Decimal -----> Binary -----|')
    selection = int(input('Enter your selection: '))

    if selection == 1:
        numbers = []
        value = str(input('Enter the value in Binary: '))
        lenght = len(value)
        for index, char in enumerate(value):
            number = int(char)
            power = pow(2, (lenght-index-1))
            resolution = number * power
            numbers.append(resolution)
        result = sum(numbers)
        print('------------------------------')
        print('                              ')
        print(f'The conversion is {result}!')
        print('                              ')
        print('------------------------------')