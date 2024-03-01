"""
Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

Crie uma instância da classe e imprima o valor da propriedade titular.

Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

Crie um método de classe para a conta ClienteBanco.
"""

from modelos.cliente_banco import ClienteBanco

class ContaBancaria:
    contas = []
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self):
        return f'{self._titular} | {self.saldo}'
    
    @classmethod
    def listar_contas(cls):
        print(f'{'Titular da Conta'.ljust(25)} | {'Saldo da Conta'.ljust(25)} | {'Status da Conta'.ljust(25)}')
        for conta in ContaBancaria.contas:
            print(f'{conta._titular.ljust(25)} | {str(conta._saldo).ljust(25)} | {conta.ativo.ljust(25)}')

    @property
    def ativo(self):
        return f'Conta Ativa' if self._ativo else 'Conta Desativada'
    
    def ativar_conta(self):
        self._ativo = not self._ativo

    

