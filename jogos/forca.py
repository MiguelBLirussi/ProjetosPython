import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavras = ['maça','banana','abacaxi','abacate','pera','kiwi','laranja','limão','caju','manga','uva',]
    num_palavra = random.randint(0,10)
    print(num_palavra)

    palavra_secreta = palavras[num_palavra].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    total_erros = letras_acertadas.count("_")
    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f'\nA palavra não possui a letra {chute}\nErros: {erros}/{total_erros}\n')
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        if acertou:
            print('Parabéns!!! Você Ganhou!!\n')
        if enforcou:
            print('Você Perdeu!! :(\nTente Novamente!!')
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()