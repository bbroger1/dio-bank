from transacao import Transacao


class Historico:
    def __init__(self, transacoes: list):
        self.transacoes = transacoes

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)

    def visualizar_historico(self, conta):
        if conta.numero_conta:
            print(f"Histórico da conta {conta.numero_conta}:")
            transacoes_da_conta = [
                t for t in self.transacoes if t.conta.numero_conta == conta.numero_conta
            ]
            for transacao in transacoes_da_conta:
                print(f"- {type(transacao).__name__}: R$ {transacao.valor:.2f}")
            print(f"# Saldo: R$ {conta.saldo:.2f}")
        else:
            print(f"Conta {conta.numero_conta} não encontrada.")
