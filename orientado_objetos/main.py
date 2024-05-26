from conta import Conta
from cliente import Cliente
from pessoaFisica import PessoaFisica
from historico import Historico


def menu():
    return """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [u] Cadastrar Cliente
        [us] Listar Clientes
        [c] Cadastrar Conta
        [q] Sair

    =>"""


def main():
    AGENCIA = "0001"
    clientes = []
    pessoas_fisicas = []
    contas = []
    numero_conta = 0
    historico = Historico([])

    while True:
        opcao = input(menu())

        if opcao == "d":
            numero_conta = int(input("Informe o número da conta: "))
            conta = Conta.verifica_conta(numero_conta, contas)
            if not conta:
                print("Conta não localizada.")
            else:
                valor = float(input("Informe o valor do depósito: "))
                print(conta.depositar(valor))

        elif opcao == "s":
            numero_conta = int(input("Informe o número da conta: "))
            conta = Conta.verifica_conta(numero_conta, contas)
            if not conta:
                print("Conta não localizada.")
            else:
                valor = float(input("Informe o valor do saque: "))
                print(conta.sacar(valor))

        elif opcao == "e":
            numero_conta = int(input("Informe o número da conta: "))
            conta = Conta.verifica_conta(numero_conta, contas)
            if not conta:
                print("Conta não localizada.")
            else:
                historico.visualizar_historico(conta)

        elif opcao == "u":
            cpf = input("CPF: ")
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento: ")
            endereco = input("Endereço: ")

            if PessoaFisica.verifica_cpf(cpf, pessoas_fisicas):
                print("CPF já cadastrado.")
            else:
                pessoa_fisica = PessoaFisica(cpf, nome, data_nascimento)
                pessoas_fisicas.append(pessoa_fisica)
                cliente = Cliente(endereco, contas, pessoa_fisica)
                clientes.append(cliente)
                print(f"Cliente {nome} cadastrado com sucesso.")

        elif opcao == "us":
            print("======== Lista de Clientes ========")
            for pf in pessoas_fisicas:
                print(f"Nome: {pf.nome} - CPF: {pf.cpf}")

        elif opcao == "c":
            cpf = input("CPF do cliente: ")
            cliente_encontrado = PessoaFisica.verifica_cpf(cpf, pessoas_fisicas)
            if not cliente_encontrado:
                print("Cliente não localizado.")
            else:
                conta = Conta(0.0, numero_conta + 1, 0, AGENCIA, cliente, historico)
                contas.append(conta)
                numero_conta += 1
                print(f"Conta de número {numero_conta} cadastrada com sucesso.")
                print(conta)

        elif opcao == "q":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
