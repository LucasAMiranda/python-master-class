# Criei um dicionario pra armazenar o numero do canal como key e a quantidade de pessoas como value
topAudiencia = {}

for i in range(1, 5):
    listaCanais = int(input("Entre com o canal desejado: "))
    porcent = 100
    casasEntrevistadas = int(input("Entre com quantidade de casas: "))
    pessoas = int(input("Quantidade de pessoas que estavam assistindo: "))

    # No final de cada execução de input os valores são adicionados lá no dicionario vazio (obs.: o numero do canal ta sendo guardado como STRING)
    topAudiencia[str(listaCanais)] = pessoas
    print(topAudiencia)


# Aqui eu crio uma nova lista, só com a quantidade de pessoas de cada canal (se for inserir os outro canais precisa adicionar eles aqui da mesma forma que o 2 e 4)
listaPessoas = [topAudiencia['2'], topAudiencia['4'],
                topAudiencia['7'], topAudiencia['9']]
# Esse comando ordena a lista, colocando o maior valor no final
listaPessoas.sort()


listaCanais = {
    # key : value
    'cultura': 2,
    'globo': 4
}


for i in topAudiencia:
    # Em listaPessoas[-1], oq tu ta fazendo é pegar o ultimo valor guardado na listaPessoas que ta ordenada, justamente o maior numero

    # Em seguida esse numero capturado é comparado com os valores do dicionario criado la em cima, se for igual, a gente pega a key dele

    # Por fim, se essa key for 2, deve retornar cultura, se for 4, deve retornar globo (obs.: se for adicionar mais, precisa fazer outros if's aqui)
    if topAudiencia[i] == listaPessoas[-1]:
        if int(i) == 2:
            print('cultura')
            break
        if int(i) == 4:
            print('globo')
            break
        if int(i) == 7:
            print('band')
            break
        if int(i) == 9:
            print('record')
            break
        else:
            print('O canal não está na lista')


totalPessoas = 0


# Total de pessoas assistindo, ele surge daqui
for i in topAudiencia:
    totalPessoas = totalPessoas + topAudiencia[i]

print(totalPessoas)  # print> 11

audienciaCultura = (topAudiencia['2']/totalPessoas)*100

audienciaGlobo = (topAudiencia['4']/totalPessoas)*100

audienciaBand = (topAudiencia['7']/totalPessoas)*100

audienciaRecord = (topAudiencia['9']/totalPessoas)*100

audienciaCultura = round(audienciaCultura, 2)
audienciaGlobo = round(audienciaGlobo, 2)
audienciaBand = round(audienciaBand, 2)
audienciaRecord = round(audienciaRecord, 2)

print(str(audienciaCultura), "%")
print(str(audienciaGlobo), "%")
print(str(audienciaBand), "%")
print(str(audienciaRecord), "%")
