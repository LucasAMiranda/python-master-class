'''
Como entrada, seu programa receberá um número inteiro L, indicando a quantidade de linhas do texto, seguido das L linhas do texto. Por último, seu programa receberá a palavra a ser buscada no texto. A palavra buscada será fornecida em letras minúsculas.

Como saída, se todas as letras da palavra buscada forem encontradas, o seu programa deverá imprimir a mensagem Palavra encontrada. Caso contrário, deverá imprimir Palavra nao encontrada. Além disso, caso a palavra for encontrada, seu programa deve fornecer, para cada letra da palavra buscada, a posição da palavra no texto e posição da letra nesta palavra onde ela foi encontrada.

Regras: 

Cada palavra do texto deverá conter no máximo uma letra da palavra buscada
As letras da palavra buscada deverão ser buscadas sequencialmente, ou seja, iniciando da primeira e terminando na última letra
As palavras do texto serão verificadas sequencialmente apenas uma única vez

'''

#Entrada de dados

L = str(input("Digite uma frase: ")).strip()


#Saída de dados
if(L.split() != False):
    print(L.split())
    print('Palavra encontrada')
    print(L.lower().find('penso'))
    print(L.lower().find('logo'))
    print(L.lower().find('existo'))
    print(L[::13])
else:
    print('Palavra nao encontrada')

