from math import pi

''' # 01 - Cálcule a área de um triangulo

base = float(input('Vamos cálcular a área do seu retângulo, qual sua base em centímetros? '))
altura = float(input('E a altura? '))

area = base * altura

print('A área do seu triângulo é de {:.0f}cm.'.format(area))

'''

''' # 02 - Cálcule a área de um quadrado

lado = float(input('Vamos cálcular a área do seu quadrado, qual o comprimento de qualquer um dos lados em centímetros? '))

print('A área do seu quadrado é de {:.0f}cm.'.format(lado * lado))

'''

''' # 03 - Cálculadora de descontos

valor = float(input('Qual o valor do total produto? '))
desconto = float(input('Quantos % de desconto você terá? '))

desconto = desconto / 100

print('O valor a ser pago é de: R${:.2f}'.format(valor - valor * desconto))

'''

''' # 04 - Cálcule a área de um círculo

raio = float(input('Vamos cálcular a área do seu círculo, qual o comprimento do raio em centímetros? '))
area = pi * (raio ** 2)

print('A área do seu círculo é de: {:.2f}cm.'.format(area))

'''

''' # 05 - Conversão BRL x USD

print('Atualmente $1,00 equivale a R$5,38.')
brl = float(input('Insira valor em reais: ').replace(',', '.'))
conv = brl / 5.38

print('R${:.2f} equivale a ${:.2f}.'.format(brl, conv))

'''

''' # 06 - Conversão USD x BRL

print('Atualmente $1,00 equivale a R$5,38.')
usd = float(input('Insira valor em dólares: ').replace(',', '.'))
conv = usd * 5.38

print('${:.2f} equivale a R${:.2f}.'.format(usd, conv))

'''
