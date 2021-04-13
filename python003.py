"""

Crie váriaveis em python que atribua valores de soma, subtração, divisão, multiplicação

"""

a = int(input("Digite o valor de a: ")) #15
b = int(input("Digite o valor de b: ")) # 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('Soma: {soma}\n Subtracao: {subtracao}\n Multiplicação: {multiplicacao}\n Divisão: {divisao}\n Resto: {resto}'
             .format(soma=soma, subtracao=subtracao, multiplicacao=multiplicacao, divisao=divisao, resto=resto ))

#resultado = ('soma: {} \n  subtração: {}\n multiplicação: {}\n divisão {}\n  resto: {} '
#.format(soma, subtracao, multiplicacao, divisao, resto))

print(resultado)


