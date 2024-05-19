def menu():

    return """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [u] Cadastrar Cliente
        [c] Cadastrar Conta
        [q] Sair

    =>"""


def depositar(conta, valor):
    if valor > 0:
        conta[1] += valor
        conta[2].append(f"Depósito: R$ {valor:.2f}")
        return "Depósito realizado com sucesso."
    else:
        return "Operação falhou! O valor informado é inválido."


def sacar(conta, valor, LIMITE_VALOR_SAQUE, LIMITE_QUANTIDADE_SAQUES):

    excedeu_saldo = valor > conta[1]
    excedeu_limite = valor > LIMITE_VALOR_SAQUE
    excedeu_saques = conta[5] >= LIMITE_QUANTIDADE_SAQUES

    if excedeu_saldo:
        return "Operação falhou! Você não tem saldo suficiente."
    elif excedeu_limite:
        return "Operação falhou! O valor do saque excede o limite."
    elif excedeu_saques:
        return "Operação falhou! Número máximo de saques excedido."
    elif valor > 0:
        conta[1] -= valor
        conta[2].append(f"Saque: R$ {valor:.2f}")
        conta[5] += 1
        return "Saque realizado com sucesso."
    else:
        return "Operação falhou! O valor informado é inválido."


def visualizar_extrato(conta):
    print(f"\n================ EXTRATO - Conta nr. {conta[3]}================")
    if not conta[2]:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in conta[2]:
            print(movimento)
    print(f"\nSaldo: R$ {conta[1]:.2f}")
    print("==========================================")


def cadastrar_cliente(nome, data_nascimento, cpf, endereco, clientes):
    cliente = [nome, data_nascimento, cpf, endereco]
    clientes.append(cliente)
    return f"Cliente {nome} cadastrado com sucesso."


def cadastrar_conta(cpf, AGENCIA, numero_conta, quantidade_saques, contas):
    conta = [AGENCIA, 0, [], numero_conta + 1, cpf, quantidade_saques]
    contas.append(conta)
    return f"Conta {conta} cadastrada com sucesso."


def verifica_conta(numero_conta, contas):
    conta_encontrada = None
    for conta in contas:
        if conta[3] == numero_conta:
            conta_encontrada = conta

    return conta_encontrada


def verifica_cpf(cpf, clientes):
    cpf_encontrado = False
    for cliente in clientes:
        if cliente[2] == cpf:
            cpf_encontrado = True

    return cpf_encontrado


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
                print(depositar(conta, valor))

        elif opcao == "s":
            numero_conta = int(input("Informe o número da conta: "))
            conta = verifica_conta(numero_conta, contas)
            if not conta:
                print("Conta não localizada.")
            else:
                valor = float(input("Informe o valor do saque: "))
                print(sacar(conta, valor, LIMITE_VALOR_SAQUE, LIMITE_QUANTIDADE_SAQUES))

        elif opcao == "e":
            numero_conta = int(input("Informe o número da conta: "))
            conta = verifica_conta(numero_conta, contas)
            if not conta:
                print("Conta não localizada.")
            else:
                visualizar_extrato(conta)

        elif opcao == "u":
            cpf = int(input("Informe o CPF do cliente (somente números): "))
            if verifica_cpf(cpf, clientes):
                print("Cliente já cadastrado.")
            else:
                nome = str(input("Informe o nome do cliente: "))
                data_nascimento = str(
                    input("Informe a data nascimento (dd-mm-aaaa) do cliente: ")
                )

                logradouro = str(input("Informe o logradouro do cliente: "))
                numero = int(input("Informe o número do logradouro do cliente: "))
                bairro = str(input("Informe o bairro do cliente: "))
                cidade = str(input("Informe a cidade do cliente: "))
                uf = str(input("Informe a uf do cliente: "))
                endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{uf}"

                print(cadastrar_cliente(nome, data_nascimento, cpf, endereco, clientes))

        elif opcao == "c":
            cpf = int(input("Informe o CPF do cliente (somente números): "))
            if not verifica_cpf(cpf, clientes):
                print("Cliente não localizado.")
            else:
                print(
                    cadastrar_conta(
                        cpf, AGENCIA, numero_conta, quantidade_saques, contas
                    )
                )

        elif opcao == "q":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
