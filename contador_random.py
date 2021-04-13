import random 

 
while True: 
    resposta =  input('você gostaria de jogar o dado?: ')
    dado = random.randrange(1, 6)
 
    if (resposta == 'N' or resposta=='NÃO'):
       print(dado)
       break

    elif(resposta == 'S' or resposta=='SIM'):
       print(dado)
     
    elif(dado != 1 or dado != 0 ):
       print('Você informou outra resposta. Tente Novamente')
 



