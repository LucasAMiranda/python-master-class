def citys():
    while True:
        DDD = int(input("Digite o seu DDD: "))

        cidades = {
            11: 'São Paulo',
            71: 'Salvador',
            21: 'Rio de Janeiro',
            32: 'Juiz de Fora',
            19: 'Campinas',
            27: 'Vitoria',
            31: 'Belo Horizonte'
        }

        if DDD in cidades:
            print('O usuario está em {}'.format(cidades[DDD]))
        else:
            print('Nao encontramos esse DDD')

if __name__ == '__main__':
    citys()