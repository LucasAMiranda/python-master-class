def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x) #verifica o Tamanho das palavras dentro da lista
        contador.append(quantidade)
    return contador

def testeContador(s):
    caracteres_ordenados =  sorted(s) #strings a serem contadas

    caracter_anterior  = caracteres_ordenados[0] # valor do primeiro caracter
    contagem = 1 #  inicia com a contagem para 1

    for caracter in  caracteres_ordenados[1:]: #iteração do caracter já começado com 1 usando o slice
        if caracter ==  caracter_anterior:
            contagem += 1  #incremento da contagem
        else:
            print(f'{caracter_anterior}:{contagem}')
            caracter_anterior =  caracter # faz a referência ao  caracter anterior
            contagem  = 1 #inicia a contagem para 1 

    print(f'{caracter_anterior}: {contagem}')

#DEBUGANDO 
if __name__ == '__main__': 
    lista = ['cachorro', 'gato', 'coelho']
    print(contador_letras(lista))
    testeContador('cachorro')
    print()
    testeContador('gato')
