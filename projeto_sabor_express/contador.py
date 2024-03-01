import os

def contador_impar():
    #feito utilizando laço de repetição "for"
    for numeros in range(1,999+1):
        if numeros % 2 != 0:
            print(numeros)

def contador_par():
    #feito utilizando laço de repetição "while"
    #feito de duas maneiras apenas pra exemplificar que é possível utilizar os dois
    #o que muda é a sintaxe a lógica permanece a mesma
    contador = 0
    while (contador < 999):
        contador += 1
        if contador % 2 == 0:
            print(contador)

def exibir_nome_do_programa():
    print('Bem vindo ao contador de números')

def exibir_opcoes ():
    print('Você deseja contar números pares ou impares?\n')
    print('1 - Impares | 2 - Pares | 3 - Sair\n')

def opcao_invalida():
    print('\nDigite uma operação valida\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def escolher_opcao ():
    try:
        par_ou_impar = int(input('Digite a operação desejada (1 | 2 | 3): '))
        if par_ou_impar < 1 or par_ou_impar > 3:
            opcao_invalida()
        elif par_ou_impar == 1:
            contador_impar()
            input('\nDigite uma tecla para voltar ao menu principal: ')
            main()
        elif par_ou_impar == 2:
            contador_par()
            input('\nDigite uma tecla para voltar ao menu principal: ')
            main()
        elif par_ou_impar == 3:
            os.system('cls')
            print('Encerrando o programa...')
    except:
        opcao_invalida()


def main():
    ''' ESSA FUNÇÃO É UTILIZADA PARA VOLTAR AO MENU PRINCIPAL '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main() 