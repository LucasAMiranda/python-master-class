max_multas = 0
total_geral = 0

while True:
    print("Digite um número da carteira de motorista(de 1 até 9999) ou -1 para terminar: ")
    carteira = int(input("Digite  o número da carteira de motorista: "))

    if carteira == -1:
        break

    total_multas = 0
    num_multas = int(input("Informe a quantidade de multas: "))

    for i in range(num_multas):
        valor_multa = float(input("Digite o valor da multa em R$: "))
        total_multas += valor_multa # total_multas = total_multas + valor_multa

    if num_multas > max_multas:
        max_multas = num_multas
        carteira_max_multas = carteira
    
    print("Carteira de Motorista: ", carteira)
    print("Valor à Pagar: ", total_multas)

    total_geral += total_multas

print("Número da carteira com maior número de multas: ", carteira_max_multas)
print("Valor total arrecadado R$ ", total_geral)

