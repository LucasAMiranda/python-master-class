import random


i = random.randrange(1, 10)

max =  int(input('Informe um número entre 1 a 10: '))
min = int(input('informe um número entre 1 a 10: '))

while i != 0:
    
    if(max > i):
        max = int(input('Informe um número entre 1 a 10: '))
        print('você chutou alto')
    
    elif(min < i):  
        min = int(input('informe um número entre 1 a 10: '))
        print('Você chutou baixo')
    
    else:
        print('parabéns! Você acertou o número')
        break
        
        


