class Animal:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print("Meu nome é", self.nome)

class Cachorro(Animal):
    def __init__(self, nome,idade):
        super().__init__(nome)
        self.idade = idade

    def latir(self):
        print("Au au!")

class Gato(Animal):
    def miar(self):
        print("Miau!")

cachorro = Cachorro("Dorota", 18)
gato = Gato("Maria Belém")

cachorro.apresentar()
cachorro.latir()
print("Idade: ",cachorro.idade)
gato.apresentar()
gato.miar()
