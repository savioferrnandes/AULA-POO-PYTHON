class Animal:
    def emitir_som(self):
        print("O animal faz um som")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

class Vaca(Animal):
    def emitir_som(self):
        print("Muuu!")

animais = [ Cachorro(), Gato(), Vaca()]
for animal in animais:
    animal.emitir_som()