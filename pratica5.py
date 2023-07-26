# Banco de dados em lista.

nome = input('nome? ')
idade = input('idade? ')
cidade = input('cidade? ')
email = input('email? ')
telefone = input('telefone? ')  # Coleta

cliente = [nome, idade, cidade, email, telefone]  # Armazenamento

print('''Código para consultas:
0(nome) 1(idade) 2(cidade) 3(email) 4(telefone)''')  # Legenda

while True:
    query = int(input('Deseja consultar o que? '))

    while query >= len(cliente) or query < 0:
        query = int(input('Erro 001: Favor inserir consulta válida: '))

    print(cliente[query])  # Looping de query's
