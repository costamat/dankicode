listapacientes = 'Lista de pacientes: \n'

class Paciente():
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome
        self.situação = 'Normal'
        if idade > 64:
            self.situação = 'Grupo de Risco'
                
    def registrar(self):
        global listapacientes
        listapacientes = listapacientes + "{0} - Nome: {1} - Idade: {2}".format(self.situação, self.nome, self.idade)
        return listapacientes

while True:

    print(listapacientes)

    nome = input('Para registrar um paciente, insira o nome do mesmo: ')
    idade = int(input('Agora sua idade: '))

    pacienteatual = Paciente(nome, idade)
    pacienteatual.registrar()
