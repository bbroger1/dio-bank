from conta import Conta
from cliente import Cliente


def cadastrar_cliente(nome, data_nascimento, cpf, endereco, clientes):
    cliente = Cliente(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)
    return f"Cliente {nome} cadastrado com sucesso."


def cadastrar_conta(cpf, agencia, numero_conta, quantidade_saques, contas):
    conta = Conta(agencia, numero_conta + 1, cpf, quantidade_saques)
    contas.append(conta)
    return f"Conta {conta.numero_conta} cadastrada com sucesso."


def verifica_conta(numero_conta, contas):
    for conta in contas:
        if conta.numero_conta == numero_conta:
            return conta
    return None


def verifica_cpf(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return True
    return False


def menu():
    return """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [u] Cadastrar Cliente
        [c] Cadastrar Conta
        [q] Sair

    =>"""


def main():
    LIMITE_QUANTIDADE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500
    AGENCIA = "0001"

    clientes = []
    contas = []
    numero_conta = 0
    quantidade_saques = 0

    while True:
        opcao = input(menu())

        if opcao == "d":
            numero_conta = int(input("Informe o número da conta: "))
            conta = verifica_conta(numero_conta, contas)
            if not conta:
                print("Conta não localizada.")
            else:
                valor = float(input("Informe o valor do depósito: "))
                print(conta.depositar(valor))

        elif opcao == "s":
            numero_conta = int(input("Informe o número da conta: "))
            conta = verifica_conta(numero_conta, contas)
            if not conta:
                print("Conta não localizada.")
            else:
                valor = float(input("Informe o valor do saque: "))
                print(conta.sacar(valor, LIMITE_VALOR_SAQUE, LIMITE_QUANTIDADE_SAQUES))

        elif opcao == "e":
            numero_conta = int(input("Informe o número da conta: "))
            conta = verifica_conta(numero_conta, contas)
            if not conta:
                print("Conta não localizada.")
            else:
                conta.visualizar_extrato()

        elif opcao == "u":
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            if verifica_cpf(cpf, clientes):
                print("CPF já cadastrado.")
            else:
                print(cadastrar_cliente(nome, data_nascimento, cpf, endereco, clientes))

        elif opcao == "c":
            cpf = input("CPF do cliente: ")
            if not verifica_cpf(cpf, clientes):
                print("Cliente não localizado.")
            else:
                quantidade_saques = 0
                numero_conta += 1
                print(
                    cadastrar_conta(
                        cpf, AGENCIA, numero_conta, quantidade_saques, contas
                    )
                )

        elif opcao == "q":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
