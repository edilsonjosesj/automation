# usuário digita um número
# informar se este é par ou impar
# se não for um número inteiro escrever mensagem na tela: ESTE NÃO É UM NÚMERO INTEIRO

InputNumber = input('Por favor, entre com um número INTEIRO: ')

if InputNumber.isnumeric():
    InputNumber = int(InputNumber)
    if (InputNumber % 2 == 0):
        print('Este é um número PAR')
    else:
        print('Este é um número IMPAR')
else:
    print('Digite um número INTEIRO...')