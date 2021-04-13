"""
O math.floor()método arredonda um número PARA BAIXO para o inteiro mais próximo, se necessário, e retorna o resultado.
    Busca Binária
    Entrada:
        numeros: array numeros em ordem crescente
        n: Quantidade de numeros no array
        procurado: numero procurado
    Saida:
        Posição do numero no array
    Pseudocódigo:
        p=1 indice da esquerda
        r=n indice da direita
        enquanto p<=r
            q = piso((p+r)/2)
            Se numeros[q] == procurado
                return q
            Senão
                Se numeros[q] > procurado
                    r = q-1
                Senão
                    p = q+1
        return NOT_FOUND
"""

import math

def busca_binaria(numeros, n , procurado):
    esquerda = 0
    direita = n-1
    while esquerda <= direita:
        meio = math.floor((esquerda + direita/2))
        if numeros[meio] == procurado:
            return meio
        else:
            if numeros[meio] > procurado:
                direita = meio - 1
            else:
                esquerda = meio + 1

    return -1

numeros = [3, 7, 10, 15, 20]
n = 10
procurado = 20
resposta = busca_binaria(numeros, n, procurado)
print(resposta)

