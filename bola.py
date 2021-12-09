'''
Exercicio 1
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor

'''

class Bola:
    def __init__(self, cor, circ, material):
        self.cor = cor
        self.circ = circ
        self.material = material
    
    def trocaCor(self,cor):
        self.cor = cor
    
    def mostraCor(self):
        return self.cor

a = Bola("azul", 2, "borracha")
print(a.mostraCor())