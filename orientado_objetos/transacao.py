from abc import ABC, abstractmethod


class Transacao(ABC):
    def __init__(self, conta):
        self.conta = conta

    @abstractmethod
    def registrar(self):
        pass


class Deposito(Transacao):
    def __init__(self, conta, valor):
        super().__init__(conta)
        self.valor = valor

    def registrar(self):
        self.conta.saldo += self.valor
        self.conta.historico.adicionar_transacao(self)
        return True


class Saque(Transacao):
    def __init__(self, conta, valor):
        super().__init__(conta)
        self.valor = valor

    def registrar(self):
        if self.conta.saldo >= self.valor:
            self.conta.saldo -= self.valor
            self.conta.historico.adicionar_transacao(self)
            return True
        return False
