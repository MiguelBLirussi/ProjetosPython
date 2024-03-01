from modelos.conta_bancaria import ContaBancaria

conta_miguel = ContaBancaria('Miguel', 1250.00)
conta_joao = ContaBancaria('Joao', 24500.00)

ContaBancaria.ativar_conta(conta_miguel)
ContaBancaria.ativar_conta(conta_joao)
ContaBancaria.listar_contas()

def main():
    pass

if __name__ == '__main__':
    main()


