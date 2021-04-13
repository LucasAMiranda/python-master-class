'''
Peça o usuário que digite três valores e armazene esses valores em uma variável a, b e c . E depois imprima o maior deles.
'''
#Definição de váriveis
a = int(input("Informe o primeiro valor: "))
b = int(input("informe o segundo  valor: "))
c = int(input("Informe o terceiro valor: "))

if(a > b and b < a and c < a):
    print('O maior é {}'. format(a)) 

elif (b > a and b > c):
    print('O maior é {}'. format(b))

else:
    print('O maior é {}'. format(c))

'''
Peça o usuário que digite dois valores, armazene esses valores em duas variáveis chamada a e b . No final imprima informe se um dos valores
digitados é par
'''
#DEFINIÇÃO VARIÁVEIS
a = int(input("informe o primeiro valor: "))
b  = int(input("informe o primeiro valor: "))

resto_a = a % 2
resto_b = a % 2

if(resto_a == 1): 
    print('O valor é ÍMPAR')

elif(resto_a == 0):
    print('O  valor é PAR')

elif(resto_b == 1):
    print('O  valor é PAR')

else:
    print('O Valor é ÍMPAR')



"""
Peça o usuário que digite 4 notas bimestrais a, b, c e d . Faça o cálculo das médias bimestrais e imprima as médias bimestrais formatadas.
"""
"""
a = int(input("Informe a primeira nota: "))
b = int(input("Informe a segunda nota: "))
c = int(input("Informe a terceira nota: "))
d = int(input("informe a quarta nota: "))

media = (a + b + c + d) / 4

if(a >= 10 and b >= 10 and c >= 10 and d >=10):
    print("O aluno atingiu acima da  média dos Bimestres\n")
    print("A média das notas bimestrais foi de: {media}".format(media=media))
elif(a < 10 and b < 10 and c < 10 and d < 10):
    print("A média das notas bimestrais foi de: {media}".format(media=media))
else:
    if (a > 10):
       a  = int(input("Favor, digitar a nota correta. Primeira nota: "))
"""