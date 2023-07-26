''' # 01 - Categorização de acordo com idade

idade = int(input('Insira sua idade: '))

if idade > 0 and idade < 16:
    print('MENOR')
elif idade >= 16 and idade < 18:
    print('EMANCIPADO')
elif idade >= 18:
    print('MAIOR')
else:
    print('Tente novamente...')

'''

''' # 02 - Categorização de acordo com idade II

idade = int(input('Insira sua idade para descobrir sua categoria: '))

if idade >= 5 and idade <= 7:
    print('Infantil A')
elif idade >= 8 and idade <= 10:
    print('Infantil B')
elif idade >= 11 and idade <= 13:
    print('Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Juvenil B')
else:
    print('Tente novamente...')

'''
