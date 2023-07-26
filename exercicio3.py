n1 = int(input('Digite 5 números. Qual o primeiro? '))
n2 = int(input('E o segundo? '))
n3 = int(input('O terceiro? '))
n4 = int(input('O quarto? '))
n5 = int(input('E o quinto? '))

numbers = [n1, n2, n3, n4, n5]

for x in numbers:
    if x >= numbers[0] and x >= numbers[1] and x >= numbers[2] and x >= numbers[3] and x >= numbers[4]:
        maior = x
    if x <= numbers[0] and x <= numbers[1] and x <= numbers[2] and x <= numbers[3] and x <= numbers[4]:
        menor = x

print('O maior é o {0}. O menor o {1}.'.format(maior, menor))