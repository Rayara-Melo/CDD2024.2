class Pessoa:
    def __init__(self, nome, peso, idade, falar=False, comer=False, dormir=False): #TUDO QUE TEM sef É UM ATRIBUTO.
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falar = falar
        self.comer = comer
        self.dormir = dormir

    def falar (self):
        print(f"{self.nome} está falando")
        self.falar == True
    def comer (self):
        print(f"{self.nome} está comendo")
        self.comer == True
    def dormir (self):
        print(f"{self.nome} está dormindo")
        self.dormir == True
