class Lavajato():

    def __init__(self):
        self.atendimentos = None
        self.Veiculo = None
        self.preco = None
        self.servico = None

    def menu(self):
        opcao = input("Escolha a opção para Gerar Atendimento: ")

        if opcao == '1':
            self.atender()
        elif opcao == '2':
            self. executar_proximo_servico()
    
    def atender(self):
        servico = str(input("Informe o tipo de serviço[lavaragem rápida ou Geral]: "))
        veiculo = str(input("Escolha o tipo de veículo: "))
        cor = str(input("Cor do veículo: "))
        placa = str(input("Placa do Veículo: "))
        if  servico == "lavagem rápida":
            atendimentos = []
            Veiculo = [servico, veiculo, cor, placa]
            atendimentos.append(Veiculo)
            print(atendimentos)

            if veiculo == 'Motos':
               preco = 20.00
               print(f"A Lavagem das {veiculo} é R$ {preco}")
            if veiculo == 'Carro de Passeio':
               preco = 30.00
               print(f"A Lavagem do {veiculo} é R$ {preco}")
            if veiculo == 'Utilitário':
               preco = 35.00
               print(f" A Lavagem do {veiculo} é R$ {preco}")
            if veiculo == 'Caminhonetes':
               preco = 40.00
               print(f" A Lavagem do {veiculo} é R$ {preco}")
            if veiculo == 'Caminhão':
               preco = 70.00
               print(f" A Lavagem do {veiculo} é R$ {preco}")


    def executar_proximo_servico(self):
            veiculo = str(input("Informe o tipo do veículo: "))  
            preco = float(input("informe o preço da lavagem do veículo: "))
            servico = str(input("Informe o tipo de serviço[lavagem rápida ou Geral]: "))
            if servico == "lavagem geral": 
               atendimentos = []
               Veiculo = [servico, veiculo, preco ]
               atendimentos.append(Veiculo)
               precoAcrescido = (preco * 10)/100
               totalPreco = precoAcrescido + preco
               print(f"A lavagem do {veiculo} é {totalPreco} reais com 10% de acréscimo")
               print(atendimentos)


while True:
   gerarAtendimento = Lavajato()
   gerarAtendimento.menu()