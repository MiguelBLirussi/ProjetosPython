class ClienteBanco:
    clientes = []
    def __init__(self, nome, idade, cpf, data_nascimento, data_abertura):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self.data_nascimento = data_nascimento
        self.data_abertura = data_abertura
        ClienteBanco.clientes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._cpf}'
    
    @classmethod
    def listar_clientes(cls):
        for cliente in ClienteBanco.clientes:
            print(f'{cliente._nome.ljust(25)} | {str(cliente._idade).ljust(25)} | {cliente._cpf}')

cliente_1 = ClienteBanco('Miguel Barreto', 12 , '39207827808', '04/10/2003', '21/01/2024' )

ClienteBanco.listar_clientes()
