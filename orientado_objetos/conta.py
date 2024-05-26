from transacao import Deposito, Saque
from historico import Historico

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cliente import Cliente

LIMITE_QUANTIDADE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500


class Conta:
    def __init__(
        self,
        saldo: float,
        numero_conta: int,
        quantidade_saques: int,
        agencia: str,
        cliente: "Cliente",
        historico: "Historico",
    ):
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.quantidade_saques = quantidade_saques
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    def sacar(self, valor: float) -> str:
        if valor > self.saldo:
            return f"Valor do saque é maior que o saldo atual."

        if valor > LIMITE_VALOR_SAQUE:
            return f"Valor do saque é maior que o limite: R$ {LIMITE_VALOR_SAQUE},00."

        if self.quantidade_saques >= LIMITE_QUANTIDADE_SAQUES:
            return "Limite de saques excedido."

        saque = Saque(self, valor)
        if saque.registrar():
            self.quantidade_saques += 1
            return f"Saque realizado com sucesso."

        return f"Saque não realizado."

    def depositar(self, valor: float) -> str:
        deposito = Deposito(self, valor)
        if deposito.registrar():
            return f"Depósito realizado com sucesso."

        return f"Depósito não realizado."

    def cadastrar_conta(
        self,
        saldo: float,
        numero_conta: int,
        quantidade_saques: int,
        agencia: str,
        cliente: "Cliente",
        historico: "Historico",
        contas: list,
    ) -> str:
        conta = Conta(
            saldo, numero_conta + 1, quantidade_saques, agencia, cliente, historico
        )
        conta.quantidade_saques = 0
        contas.append(conta)
        return f"Conta {conta.numero_conta} cadastrada com sucesso."

    @staticmethod
    def verifica_conta(numero_conta: int, contas: list):
        for conta in contas:
            if conta.numero_conta == numero_conta:
                return conta
        return None

    def __str__(self) -> str:
        return f"""Conta Nº {self.numero_conta} 
            Agência: {self.agencia}
            Saldo: R$ {self.saldo:.2f}
            Quantidade de Saques: {self.quantidade_saques} """
