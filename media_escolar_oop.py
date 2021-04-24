class Escola:
    def __init__(self, nota, media, nomeAluno):
        self.nota = nota
        self.nomeAluno = nomeAluno
        self.media = media
        self.listarNotas()

    def listarNotas(self):
        contador = 0
        for nome in self.nomeAluno:
            self.mostrarMedia(nome, self.nota[contador]) # nome e a nota da lista que vão ser armazenados
            contador += 1

    def mostrarMedia(self, nome, nota):
        if nota >= self.media:
            print("Aluno: {},\nnota: {},\n::aprovado".format(nome, nota))
        else:
            print("Aluno: {},\nnota: {},\n::reprovado".format(nome, nota))


contador = int(input('Digite quantos alunos vão ter: '))
num = 0
nomeA = []
notaA = []

while num < contador:
    nome = input('Digite o nome: ')
    nota = int(input('Digite a nota: '))
    nomeA.append(nome)
    notaA.append(nota)
    num += 1

escola = Escola(nota=notaA, media=4, nomeAluno=nomeA)
