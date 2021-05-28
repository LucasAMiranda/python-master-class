def fizzbuzz(n):
    """
        >>> fizzbuzz(7)
        1
        fizz
        buzz
        fizz
        5
        fizzbuzz
        7
        >>> fizzbuzz(2)
        1
        fizz

        :param: n
        :return: 
    """

    lista = []
    for i in range(1 , n + 1): 
        resultado = ''
        if  i % 2==0:
            resultado == 'fizz'
        if i % 3 == 0:
            resultado += 'buzz'
        if resultado == '':
            resultado = i
        lista.append(resultado)
    return lista

print (fizzbuzz(7))

