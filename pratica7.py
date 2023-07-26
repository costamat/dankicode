class Carro():
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def Partida(self):
        print('Ligando...')

    def AbirJanelas(self):
        print('Abrindo janelas')
    
    def ArCondicionado(self):
        print('Ligando ar condicionado')
        

carro1 = Carro('Chevrolet', 'Chevette', 'Branco')

print(carro1.__dict__)

carro1.Partida()
carro1.AbirJanelas()
carro1.ArCondicionado()
