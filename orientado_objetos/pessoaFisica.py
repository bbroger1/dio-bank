class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: str):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def cadastrar_pessoa_fisica(self, cpf, nome, data_nascimento, pessoas_fisicas):
        pf = PessoaFisica(cpf, nome, data_nascimento)
        pessoas_fisicas.append(pf)
        return f"Pessoa física {nome} cadastrado com sucesso."

    @staticmethod
    def verifica_cpf(cpf: str, pessoas_fisicas: list):
        for pessoa_fisica in pessoas_fisicas:
            if pessoa_fisica.cpf == cpf:
                return True
        return False
