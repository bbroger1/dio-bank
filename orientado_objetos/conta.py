class Conta:
    def __init__(self, agencia, numero_conta, cpf, quantidade_saques):
        self.agencia = agencia
        self.saldo = 0
        self.movimentacoes = []
        self.numero_conta = numero_conta
        self.cpf = cpf
        self.quantidade_saques = quantidade_saques

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.movimentacoes.append(f"Depósito: R$ {valor:.2f}")
            return "Depósito realizado com sucesso."
        else:
            return "Operação falhou! O valor informado é inválido."

    def sacar(self, valor, limite_valor_saque, limite_quantidade_saques):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > limite_valor_saque
        excedeu_saques = self.quantidade_saques >= limite_quantidade_saques

        if excedeu_saldo:
            return "Operação falhou! Você não tem saldo suficiente."
        elif excedeu_limite:
            return "Operação falhou! O valor do saque excede o limite."
        elif excedeu_saques:
            return "Operação falhou! Número máximo de saques excedido."
        elif valor > 0:
            self.saldo -= valor
            self.movimentacoes.append(f"Saque: R$ {valor:.2f}")
            self.quantidade_saques += 1
            return "Saque realizado com sucesso."
        else:
            return "Operação falhou! O valor informado é inválido."

    def visualizar_extrato(self):
        print(
            f"\n================ EXTRATO - Conta nr. {self.numero_conta}================"
        )
        if not self.movimentacoes:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.movimentacoes:
                print(movimento)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")
