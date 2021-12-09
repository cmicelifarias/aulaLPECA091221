class Retangulo:
    def __init__(self,lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    
    def Area(self):
        return self.lado1*self.lado2

class Quadrado(Retangulo):
    def __init__(self,lado):
        self.lado = lado
    '''
    ** -> assim
    pow() ou math.power -> usando import math
    numpy.np() -> usando numpy
    '''
    def Area(self):
        return self.lado* self.lado

a = Quadrado(2)
print(a.Area())