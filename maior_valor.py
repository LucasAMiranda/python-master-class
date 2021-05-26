#FAÇA UM ALGORITMO PARA LER O CÓDIGO 
#E O PREÇO DE 15 PRODUTOS , CALCULAR  E ESCREVER 
# - O maior preço lido
# - A média aritmética dos preços dos produtos

soma = 0
maior = 0
for x in range(1, 15+1):
	cod = int(input("Informe o código: "))
	valor = int(input("Infome o valor: "))
	if valor > maior:
		soma = soma + valor
		maior = valor 


print("O maior valor é ", maior)
print("A soma aritmética do valores dos produtos é ", soma)