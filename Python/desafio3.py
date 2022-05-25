#menor igual a 4
#entre 4 e 6 letras
#maior que 6

InputName = input('Enter your name: \n')

if len(InputName) != 0:
    
    if len(InputName) <= 4:
        print(f'{InputName} is a short name')
    elif len(InputName) >= 4 and len(InputName) <= 6:
        print(f'{InputName} is a medium size name')
    elif len(InputName) > 6:
        print(f'{InputName} is a big name')
else:
    print("Please, enter your name. It's empty")

