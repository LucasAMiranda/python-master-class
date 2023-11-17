import random 

def chuteNumero():

    i = random.randrange(1, 10)

    while True:
        respost = int(input('Digite um número entre 1 e 10: '))

        if (respost > i):
            print('Tente Novamente. Está quase lá!')
            break
            
        elif (respost < i):
            print('Parabéns! Você acertou o número')
            break
            
        else:
            print("Você chutou alto")
            break
            

    option = input('Deseja continuar com Jogo chute número. Digite SIM(S) ou Não(N): ')
    if option.upper() == 'S':
       return chuteNumero()
    else:
        print("O jogo foi encerrado.")

if __name__ == '__main__':
    chuteNumero()