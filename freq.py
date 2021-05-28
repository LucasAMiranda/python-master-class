'''
#Programação Linear 
'''

from functools import reduce


def freq(s):
    def contar_letra(resultado, letra):
        resultado[letra] = resultado.get(letra, 0) + 1
        return resultado

    return reduce(contar_letra, s, {})

print(freq('banana'))
