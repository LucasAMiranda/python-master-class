def forExamples():
    print("---Example 1---")
    for counter in range(1,10):
        print(counter)
    print()
    print("---Example 2---")
    for counter in range(2, 11, 2):
        print(counter)
    print()
    print("---Example 3---")
    for counter in range(1, 11):
        print(counter, end='')

    print("---Example 4----")
    numeros = [i for i in range(0,10)]
    print(numeros)
    print()
    numeros_pares = [i for i in range(0,10) if not i % 2]
    print(numeros_pares)
    print()
    numeros_impares = [i for i in range(10) if i % 2]
    print(numeros_impares)

    print("---Example5---")
    numerosPares = []
    for i in range(0,10):
        if(i%2==0):
            numerosPares.append(i)
    print(numerosPares)

if __name__ == '__main__':
    forExamples()