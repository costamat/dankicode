numero = int(input("Escreva um número para achar seu fatorial: "))
fatorial = numero
multiplicador = numero - 1
execfatorial = 1

while multiplicador != 0:
    if numero == 0:
        fatorial = 1
        multiplicador = 0
        break
    elif numero < 0:
        execfatorial = 0
        print('Nao existe fatorial de numeros negativos.')
        break
    fatorial *= multiplicador
    multiplicador = multiplicador - 1

if execfatorial == 1:
    print(f"O fatorial de {numero} é: {fatorial}.")
