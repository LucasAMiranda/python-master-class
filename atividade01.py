#Ler os dados 12 vezes
for i in range(1, 13):
    #Entrada de dados
    N = input("Infome o número de itens: ")
    W = input("Informe a capacidade máxima: ")

    #Escolha dos itens da mochila
    pesos_itens = [300, 400, 600, 1300, 2000]
    valores_itens = [100, 400, 300, 700, 2000]

    soma_valores = valores_itens[1] + valores_itens[2] + valores_itens[4]
    soma_pesos = pesos_itens[1] + pesos_itens[2] + pesos_itens[4]

    #Escolhe item com menor peso em caso de empate
    #guarda - chuva = 400
    #livro = 2000
    #valor/peso

    if (valores_itens[1] == valores_itens[4]):
        menor_peso = valores_itens[4] / pesos_itens[4]
        print("O item de menor peso é o livro com " +str(menor_peso) + " gramas")
    else:
        menor_peso = valores_itens[1]
        print("O item de menor peso é o guarda-chuva com " +str(menor_peso)+ " gramas")

    #saida de dados
    print(soma_valores)
    print(soma_pesos)
