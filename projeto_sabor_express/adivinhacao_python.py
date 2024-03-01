import random

print('Bem vindo ao jogo de advinhação !!')
print('Para começar escolha a dificuldade do jogo\n')

numero_secreto = random.randrange(1,100)
tentativa =0
contador = 1
opcao_valida = False
pontos = 1000

while opcao_valida != True:
    try:
        dificuldade = int(input('(1)- facil  (2)-normal (3)-dificil: '))

        if(dificuldade < 1 or dificuldade > 3):
            print('Escolha  uma opção entre 1 e 3 ')
        else:
            if(dificuldade == 1):
                tentativa = 20
            elif(dificuldade == 2):
                tentativa = 10
            else:
                tentativa = 5
            opcao_valida = True
    except:
        print('Opção invalida!! escolha  uma opção entre 1 e 3')

while(contador <= tentativa):
    print(f'Você esta na tetantiva {contador} de {tentativa}\n')
    print('Escolha um numero entre 1 e 100!\n')
    try:
        chute = int(input('Digite o seu chute: '))

        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(chute < 1 or chute > 100):
            print('Numero invalido !!')

        elif(chute == numero_secreto ):
            print('PARABENS VOCÊ GANHOU !!!')
            print(f'Você finalizou com {pontos}!!!')
            break
        elif menor :
            print('Você errou, o numero chutado é MENOR! tente novamente')
            pontos_perdidos = abs(chute - numero_secreto)
            print(f'Você perdeu {pontos_perdidos} pontos!')
            pontos =  abs((numero_secreto-chute )- pontos)
        elif maior:
            print('Você errou, o numero chutado é MAIOR! tente novamente')
            pontos_perdidos = abs(chute - numero_secreto)
            print(f'Você perdeu {pontos_perdidos} pontos!')
            pontos =  abs((chute - numero_secreto )- pontos)
    except:
        print('Opção invalida')
    contador +=1