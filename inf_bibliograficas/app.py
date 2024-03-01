import re
import os

def mensagem_inicial():
#EXIBE ESSA SIMPÁTICA MENSAGEM AO INCIAR O PROGRAMA

    print('\n*** Vamos fazer o seu cadastro*** \n')
    print('Precisamos de algumas informações para concluir\n')
    print('Não se preocupe, não deve demorar muito!!\n')

def solicitar_nome():
#SOLICITAR NOME

    nome = input('Qual seu nome completo?\n')
    return nome

def validador_nome(nome):
#VALIDADOR NOME -------> TRANSFORMANDO A STRING DIGITADA PELO USUARIO EM OPERADOR BOOL DE ACORDO COM A CONDIÇÃO DO REGEX

    nome_alterado = nome.replace(' ','')
    regex = r'^\w+$'
    if re.findall(regex,nome_alterado):
        regex = r'^\D+$'
        if re.findall(regex,nome_alterado):
            return True
        else:
            return False
    else:
        return False

def verifica_nome(nome):
#VERIFICA NOME JUNTO DO USUARIO, CASO NÃO SEJA VÁLIDA REALIZA O PROCESSO NOVAMENTE

    if validador_nome(nome):
        print('\nNome Válido!')
    else:
        print('Digite um nome válido')

def exibir_nome(nome):
#EXIBE O NOME DIGITADO E VALIDADO NA TELA

    print(f'- Nome: {nome}')

def solicitar_data_nascimento():
#SOLICITAR DATA DE NASCIMENTO
    
    data_nascimento = input('\nQual sua data de nascimento("DD/MM/AAAA"): ')
    return data_nascimento

#VALIDADOR DATA -----> TRANSFORMANDO A STRING DIGITADA PELO USUARIO EM OPERADOR BOOL DE ACORDO COM A CONDIÇÃO DO REGEX
def validador_data(data_nascimento):
    regex = r'\d{2}\/\d{2}\/\d{4}$'
    return True if re.findall(regex,data_nascimento) else False

def verifica_data(data_nascimento):
#VERIFICA DATA JUNTO DO USUARIO, CASO NÃO SEJA VÁLIDA REALIZA O PROCESSO NOVAMENTE

    if validador_data(data_nascimento):
        print('\nData Válida!\n')
    else:
        print('\nDigite uma data válida no formato"DD/MM/AAAA"\n')

def exibir_data(data_nascimento):
#ALTERA A DATA DD/MM/AAAA para Data por extenso "dia" de "mes" de "ano" e EXIBE O RESULTADO

    meses = [None,'Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    dia = data_nascimento[0:2]
    mes = data_nascimento[3:5]
    mes = int(mes)
    ano = data_nascimento[6:]
    data_nascimento = (f'- Data de Nascimento: {dia} de {meses[mes]} de {ano}')
    print(data_nascimento)



def solicitar_endereco():
#SOLICITA ENDEREÇO

    print('\nAgora falta pouco, vamos cadastrar seu endereço!\n')
    rua = input('Primeiro me informe sua rua: \n')
    numero_casa = input('Qual o número da casa?\n')
    cidade = input('Qual a cidade?\n')
    endereco = f'{rua}, {numero_casa}, {cidade}'
    return endereco


def validador_endereco(endereco):
#VALIDADOR DO ENDEREÇO -----> TRANSFORMANDO A STRING DIGITADA PELO USUARIO EM OPERADOR BOOL DE ACORDO COM A CONDIÇÃO DO REGEX

    endereco_alterado = endereco.replace(' ','')
    regex = r'^\S+.\d+.\S+'
    return True if re.findall(regex,endereco_alterado) else False

def verifica_endereco(endereco):
#VERIFICA ENDEREÇO JUNTO DO USUARIO, CASO NÃO SEJA VÁLIDA REALIZA O PROCESSO NOVAMENTE

    if validador_endereco(endereco):
        print('\nEndereço Válido!\n')
    else:
        print('\nDigite um endereço válido!!"\n')

def exibir_endereco(endereco):
#EXIBE O ENDEREÇO DIGITADO E VALIDADO NA TELA
        print(f'- Endereço: {endereco}')



def solicitar_objetivos():
    objetivos = input('Qual o seu maior objetivo no momento?\n')
    return objetivos

def exibir_objetivos(objetivos):
    print(f'- Objetivos: {objetivos}')


def main():

#CÓDIGO PRINCIPAL
    os.system('cls')

    mensagem_inicial()

    nome = solicitar_nome()
    validador_nome(nome)
    verifica_nome(nome)

    while validador_nome(nome) == False:
        nome = solicitar_nome() 
        verifica_nome(nome)
    
    os.system('cls')
    data_nascimento = solicitar_data_nascimento()
    validador_data(data_nascimento)
    verifica_data(data_nascimento)

    while validador_data(data_nascimento) == False:
        data_nascimento = solicitar_data_nascimento()
        verifica_data(data_nascimento)

    os.system('cls')
    endereco = solicitar_endereco()
    validador_endereco(endereco)
    verifica_endereco(endereco)

    while validador_endereco(endereco) == False:
        endereco = solicitar_endereco()
        verifica_endereco(endereco)

    os.system('cls')
    objetivos = solicitar_objetivos()
    
#EXIBIR RESULTADO FINAL
    os.system('cls')
    exibir_nome(nome)
    exibir_data(data_nascimento)
    exibir_endereco(endereco)
    exibir_objetivos(objetivos)

if __name__ == '__main__':
    main()