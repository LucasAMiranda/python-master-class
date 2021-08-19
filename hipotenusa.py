cateto_oposto = float(input('Entre com o valor do cateto oposto: '))
cateto_adjacente = float(input('Entre com o valor do cateto adjacente: '))

hipotenusa = (cateto_adjacente ** 2 + cateto_oposto ** 2) ** (1/2)

print("\n==============================\n")

print("O valor da hipotenusa é: {:.2f}".format(hipotenusa))