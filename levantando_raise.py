try:
    raise NameError('Exceção foi encontrada!')

except NameError:
    print('Uma exceção passou voando!')
    raise