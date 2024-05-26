from pessoaFisica import PessoaFisica
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conta import Conta


class Cliente:
    def __init__(self, endereco: str, contas: list, pessoa_fisica: "PessoaFisica"):
        self.endereco = endereco
        self.contas = contas
        self.pessoa_fisica = pessoa_fisica

    def adicionar_conta(self, conta: "Conta"):
        self.contas.append(conta)

    def cadastrar_cliente(self, endereco, pessoa_fisica, contas, clientes):
        cliente = Cliente(endereco, pessoa_fisica, contas)
        clientes.append(cliente)
        return f"Cliente {cliente.pessoa_fisica.nome} cadastrado com sucesso."
