#Algoritmo: A viagem 
""" O seu programa irá receber dois inteiros N e W, um em cada linha, representando o número de itens e a capacidade da mochila, respectivamente. 

Em seguida o programa receberá N linhas com números inteiros representando os pesos dos itens e N linhas com números inteiros representando os valores dos itens. Os itens estarão ordenados pelo peso.

 A saída deve informar dois números inteiros (um por linha): um com a soma dos valores correspondentes aos objetos colocados na mochila e outro com a soma dos pesos dos objetos colocados na mochila.
 """
def mochila(W, N, val, n):

    #Aqui vai percorrer toda a lista do código sempre somando + 1 e adicionando valor do peso a W dentro da mochila
    #Guardando o valor em forma de lista
    M = [[0 for x in range(W + 1)] for x in range(n + 1)]

    
    #Aqui criei dois 'for' um que verifica o valor possível e outro que verifica o peso e a capacidade máxima
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0: #condicão que verifica se valor for igual a 0 ou a capacida máxima que cabe na bolsa for igual 0 
                M[i][w] = 0 #Guarda os valores em índices na sua referida posição

            if N[i-1] <= w: #N recebe o valor da capacidade da bolsa  se for menor ou igual a capacidade máxima
                M[i][w] = max(val[i-1] + M[i-1][w-N[i-1]], M[i-1][w]) # verifica os valores máximos fazendo os cálculos para dentro da mochila 

            else: # caso contrário , a Mochila vai receber a capacidade de 2700 que é a ideal para bolsa
                M[i][w] = M[i-1][w]
    return M[n][W]

#Saída de dados e escolha de itens da mochila
val = [100, 400, 300, 700, 2000]
N = [300, 400, 600, 1300, 2000]
W = 3000
n = len(val)
print(mochila(W, N, val, n))



        

 


