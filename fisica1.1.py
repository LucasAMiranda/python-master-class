nome = str(input("Informe seu nome: "))
sobrenome = str(input("Informe seu sobrenome: "))
idade = int(input("Informe sua idade: "))


def MostrarResultado():

    determinarDiaVacina(idade, nome, sobrenome)


def determinarDiaVacina(idade, nome, sobrenome):

    if nome[0] =='R' and sobrenome[-1] == 'S'.upper():
        if idade < 18:
            print("Tomar a vacina no dia 10")
    if nome[0] == 'R' and sobrenome[-1] == 'S'.upper():
        if idade > 18:
            print("Tomar a vacina no dia 14").upper()
    if nome[0] == 'R' or sobrenome[-1] == 'S':
        if idade > 18:
            print("Tomar a vacina no dia 13")


print('\n')
print("A sua idade é de {} anos seu nome começa com {} e seu sobrenome termina com {}".format(
    idade, nome[0], sobrenome[-1]))

MostrarResultado()
