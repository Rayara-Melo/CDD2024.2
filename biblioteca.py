class Pessoa:
    def __init__(self, nome, peso, idade): #TUDO QUE TEM sef É UM ATRIBUTO.
        self.nome=nome
        self.peso=peso
        self.idade=idade
    def comer (self):
        print(f"{self.nome} foi comer")
    def dormir (self):
        print(f"{self.nome} foi dormir")
    def andar (self):
        print(f"{self.nome} foi andar")
