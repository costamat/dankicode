# Codificação simples

cod = str(input('Escreva uma senha para a codificação: '))
newcod = ''

for letra in cod:
    if letra in 'Ii':
        newcod = newcod + '1'
    elif letra in 'Ee':
        newcod = newcod + '3'
    elif letra in 'Aa':
        newcod = newcod + '4'
    elif letra in 'Ss':
        newcod = newcod + '5'
    elif letra in 'Tt':
        newcod = newcod + '7'
    elif letra in 'Bb':
        newcod = newcod + '8'
    elif letra in 'Oo':
        newcod = newcod + '0'
    else:
        newcod = newcod + letra

print(f"Sua nova senha será: '{newcod}'")
