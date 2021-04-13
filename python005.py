"""
for in range
A função do comando range do python é retornar uma sequência de números por padrão de um a um  

Percorra um número de digitado pelo usuário e informe se ele é primo ou não
"""

""" 
a  = int(input("Digite um número qualquer: "))

div = 0

for x in range(1, a+1):
    resto = a % x #esse trecho faz o cálculo do resto da divisão do número digitado
    if(resto == 0):
        div += 1 #Faz a contagem do número divisível por 1 ou ele mesmo

if div == 2:
    print("O número digitado {} é primo ".format(a))
else:
    print("O número digitado {} não é primo". format(a))
 """

""" resultado = 0 
for x in range(1, 10):
     if x < 9:
       resultado += 1
       print(resultado)
"""

"""
Comando while 

"""
a = int(input("informe a primeira nota: "))
while(a > 10):
    a = int(input("Tente novamente.  Digite outra nota válida: "))
b = int(input("informe a segunda nota: "))
while(b > 10):
    b= int(input("Tente novamente.  Digite outra nota válida: "))

c = int(input("informe a terceira nota: "))
while(c > 10):
    c = int(input("Tente novamente.  Digite outra nota válida: "))

d= int(input("informe a quarta nota: "))
while(d > 10):
    d = int(input("Tente novamente.  Digite outra nota válida: "))

media = (a + b + c + d) / 4

print("A média {}".format(media))


