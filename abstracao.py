from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class Pix(Pagamento):
    def pagar(self, valor):
        print("Pagamento de R$", valor, "realizado via Pix")

class Cartao(Pagamento):
    def pagar(self, valor):
        print("Pagamento de R$", valor,"realizado via Cartão")

pagamento1 = Pix()
pagamento2 = Cartao()

pagamento1.pagar(100)
pagamento2.pagar(250)