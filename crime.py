
#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


opcao = int(input("Escolha um número: "))

listas = {
    
    'a': 'Telefonou para vítima?',
    'b': "Esteve no local do crime?",
    'c': "Mora perto da vítima?",
    'd': "Devia para vítima?",
    'e': "Já trabalhou com a vítima?" ,
    
}
    
questoes = []

if opcao == 1 or opcao==2: 
    questoes.append(listas['a'])
    questoes.append(listas['b'])
    print("suspeita")

elif opcao == 3 or opcao == 4 :
    questoes.append(listas['c'])
    print("cúmplice")

elif opcao == 5:
    questoes.append(listas['d'])
    print("Assassino")

else:
    print("Inocente")