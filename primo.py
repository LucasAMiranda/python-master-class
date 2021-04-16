num = int(input("Digite um número qualquer"))
divTot = 0

for i in range(1, num+1):
    if num % i == 0:
        print( i, " é primo ")
        divTot += 1
    else:
        print( i, " não é primo")

if divTot == 2:
    print("é por isso que ele é primo")
else:
    print("é por isso que o número {} foi dividido {} vezes e não é primo.". format(num, divTot))

