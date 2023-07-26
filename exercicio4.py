def maiorValor(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "Os dois valores são iguais."


def mediaAritmetica(x, y):
    return (x + y) / 2


def potenciacao(x, y):
    num = x
    for n in range(y-1):
        num *= x
    return num


print('Descubra o maior valor e a média aritmética.')

x = int(input('Entre com dois valores. O primeiro: '))
y = int(input('Segundo: '))
print('-' * 40)

print(maiorValor(x, y))
print(mediaAritmetica(x, y))

'''

print('Cálculo de potenciação')

x = int(input('Entre com a base: '))
y = int(input('Agora o expoente: '))

print(potenciacao(x, y))

'''