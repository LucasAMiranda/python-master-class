from python008_contadordeletras import contador_letras, testeContador

if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'coelho']
    total_letras = contador_letras(lista)
    print("O total de letras por palavra de lista {}". format(total_letras))
    print()
    