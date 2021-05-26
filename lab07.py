###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - A Viagem
# Nome: 
# RA: 
###################################################

# Leitura de Dados

n = int(input())   # Quantidade de itens
W = int(input())   # Capacidade da mochila
peso = []
valor = []
for i in range(n):
    peso.append( int(input()) )  # Leitura de n valores de peso
for i in range(n):
    valor.append( int(input()) ) # Leitura de n valores de valor

razao = []         # lista que serão adicionadas as razões valor/peso 
mochila_peso = 0   # somatória do peso dos itens na mochila
mochila_valor = 0  # somatória do valor dos itens na mochila

for i in range(n):    # adicionando os n valores de razão na lista razao
    razao.append(valor[i]/peso[i])  


# Escolha de itens pela razão

for i in range(n):    # para os n itens na mochila
    # Procura o indice do valor máximo, é importante notar que o index ira achar o primeiro valor máximo caso aja empate
    # e ja que a os itens estão ordenados por peso, iremos pegar o que tiver menor peso
    indice_maximo = razao.index(max(razao))

    if peso[indice_maximo] <= W:   # Se o peso do item for menor que a capacidade da mochila, é adicionado o item
        mochila_peso += peso[indice_maximo]   # soma o peso do item na somatória de pesos
        mochila_valor += valor[indice_maximo] # soma o valor do item na somatória de valores
        W -= peso[indice_maximo]  # diminui a capacidade da mochila
    
    # transforma a razão do item em 0, assim "eliminando" o item da lista, colocado ou não na mochila
    razao[indice_maximo] = 0  
        

# Impressão dos resultados

print(mochila_valor)
print(mochila_peso)
