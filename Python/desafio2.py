#pergunte a hora ao usuário
#0-11 bom dia 12-17 boa tarde 18-23 boa noite

InputTime = input('Quantas horas agora? entre no formato HH:MM \n')

if len(InputTime) == 5:

    if (int(InputTime[0:2])) >= 00 and (int(InputTime[0:2])) <= 11:
        print('Um bom dia pra vc!')
    elif (int(InputTime[0:2])) >= 12 and (int(InputTime[0:2])) <= 17:
        print('Uma boa tarde pra vc!!!')
    elif (int(InputTime[0:2])) >= 18 and (int(InputTime[0:2])) <= 23:
        print('Uma boa noite pra vc!!!')
else:

    print('Por favor, entre no formato HH:MM')