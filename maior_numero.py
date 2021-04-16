maior_num = int(input("informe o número: "))
menor_num = int(input("Informe outro número: "))
for x in range(1, maior_num):
    if x > maior_num:
        maior_num = x
for i in range(1, menor_num):    
    if i < menor_num:
        menor_num = i

print("O maior número é {}". format(maior_num))
print("O menor número é {}". format(menor_num))


'''
alunos = ['Hugo', 'Larissa', 'Igor']

for aluno in alunos: 
    alunos.append("Gustavo") 
    print(alunos)
    break
'''