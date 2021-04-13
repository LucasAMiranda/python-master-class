while True:
    try:
        data = int(input('porfavor, informe um número: '))
        break
    
    except ValueError:
        print('Ops! Esse número não é válido. Tente novamente.')