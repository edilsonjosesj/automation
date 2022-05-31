InputNumer = input('Enter a number: ')
InputSecondNumer = input('Enter other number: ')

if InputNumer.isnumeric() and InputSecondNumer.isnumeric():
    
    InputNumer = int(InputNumer)
    InputSecondNumer = int(InputSecondNumer)

    print(InputNumer + InputSecondNumer)
else:
    print('It can not be converted in a number')