class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        #seria a solução
        self.dict = {nome:[peso,idade]}

    def getnome(self):
        return self.nome
    
    def getpeso(self):
        return self.peso
    
    def getidade(self):
        return self.idade
        
    def retorna_elemento(self):
        x = input("diga o elemmento a ser retornado")
        if x == "nome":
            return self.dict[nome]
        elif x == "idade":
            return self.dict[nome][1]
        elif x == "peso":
            return self.dict[nome][0]
        else:
            return "valor incorreto"