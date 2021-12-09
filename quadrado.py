'''
Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; 
'''

class Quadrado:
    def __init__(self,lado):
        self.lado = lado
        
    def mudavalor(self,valor):
        self.lado = valor

    def retornalado(self):
        return self.lado

    def calculaArea(self):
        temp = self.lado
        return temp*temp

a = Quadrado(2)
print(a.calculaArea())
