a = int(input("Informe a: "));
b = int(input("Informe b: "));
c = int(input("Informe c: "));

x = 99999
while True:
    x = input().split()
    if x == ['0']:
        break
    a,b,c = x

    a, b, c = int(a), int(b), int(c)
   
   
    A = a * b
    t = A *100 / c
    t = (t) ** (1/5)
    print(int(t))




n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1


if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)
