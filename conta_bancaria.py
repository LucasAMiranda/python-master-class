class Conta:
    def __init__(self, numero, cpf, nometitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nometitular = nometitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            print('Você não tem saldo suficiente pra sacar!')
        else:
            self.saldo -= valor

    def gerarextrato(self):
        print(f"Numero: {self.numero}\nCPF: {self.cpf}\nSaldo: {self.saldo}")

    def transferevalor(self, contadestino, valor):
        if self.saldo < valor:
            print("Saldo Insuficiente")
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            return "Tranferencia realizada"


# Criação da Conta1
Conta1 = Conta(1323211312, 123456789, 'Lucas', 5000)

# Criação da Conta2
Conta2 = Conta(342323232, 1234234232, 'Mateus', 3000)

# Extratos
print('Conta1')
Conta1.gerarextrato()
print('\n')

print('Conta2')
Conta2.gerarextrato()
print()



# Realizando transferência

Conta1.transferevalor(Conta2, 2000)

# Verificando se o saldo da Conta1 foi diminuido
print('Conta1 após transferir 2000 para a Conta2')
Conta1.gerarextrato()

         