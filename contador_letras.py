def contador_letras(lista_palavras):
    contador = []

    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

def teste_contador(s):
    caracteres_ordenados = sorted(s)
    
    caractere_anterior = caracteres_ordenados
    contagem = 1 
    
    for caracter in caracteres_ordenados[1:]: #iterar do caractere já começando com 1 usando o slice
        if caracter == caractere_anterior:
            contagem += 1
        else:
            print(f'{caractere_anterior}: {contagem}')
            caractere_anterior = caracter
            contagem = 1
    
    print(f'{caractere_anterior}: {contagem}')

if __name__ == '__main__':  
    lista = ['cachorro', 'gato', 'coelho']
    print(contador_letras(lista))
    teste_contador('gato')
    print()
    teste_contador('cachorro')
    print()
    teste_contador('coelho')