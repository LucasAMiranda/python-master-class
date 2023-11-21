#Implemente um sistema de busca para um programa.
#Isto é, se o usuário digitar 4, procure um determinado usuário pelo seu CPF.

def busca_cpf():
    
    while True: 
        dados_cpf = {
            'Lucas': '012.525.844-58',
            'Marcelo': '030.343.343-25',
            'Tayse': '324.545.454-45'
        }

        opcao = int(input("Digite o 4 para buscar o cpf"))

        nome = input("Digite seu nome: ")

        if opcao == 4 and nome == 'Lucas':
            print(dados_cpf['Lucas'])
        
        
        elif opcao == 4 and nome == 'Marcelo':
            print(dados_cpf['Marcelo'])
           

        elif opcao == 4 and nome == 'Tayse':
            print(dados_cpf['Tayse'])
        
        else:
            print(f"CPF do(a) {nome} não está cadastrado no nosso Banco de dados.")
            

if __name__ == '__main__':
    busca_cpf()
