
#Listas e Tuplas em Python

"""lista_animal = ['cachorro', 'gato', 'elefante', 'cobra']

if 'lobo' in lista_animal:
    print('Existe um lobo dentro da lista animal')
else:
    print('Infelizmente, não temos o lobo na lista animal. Inserindo o lobo!')
    lista_animal.append('lobo')
    print(lista_animal)
    lista_animal.pop()
    print(lista_animal)

lista_animal.remove('elefante')
print(lista_animal) 

lista_animal[0] = 'macaco'
print(lista_animal)
"""

#Tuplas são imutáveis, ou seja você não pode alterar o elemento dentro dele


""" tupla = (1, 3, 5, 7)
print(len(tupla))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal) """

#Imprima dentro da lista somente os elementos ímpares

lista = [3,5,7,10,11]
resultado = []
for x in lista:
    if x % 2 == 1:
        print("O valor de x: {}". format(x))

