#Função para cálculo das raízes
def raizes(a, b, c):
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)

    print('\nValor de x1: {0}'.format(x1))
    print('Valor de x2: {0}'.format(x2))


#Debugando 
if __name__ == '__main__':
    while True:
        print('Calculando as raízes de uma equação de 2º grau\n')
        a = float(input('Entre com o valor de a: '))
        b = float(input('Entre com o valor de b: '))
        c = float(input('Entre com o valor de c: '))
        raizes(a,b,c)

        continua = input('Deseja sair? Digite q ou Enter para novo cálculo:')
        if (continua == 'q'):
            break