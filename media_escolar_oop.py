class Escola:

    def mostrarResultado(self):
        self.mostrarNotas()
        self.mostrarResultado()

    def __init__(self, nota, nomeAluno, media):
        self.nota = nota
        self.nomeAluno = nomeAluno
        self.media = media
        self.mostrarResultado()

    def mostrarNotas(self):
        self.listarNotas('nota')
        self.mostrarMedia()

    def listarNotas(self,  nota):
        self.notas = []
        self.notas.append(self.nota)
        self.nota.split(",")
        for notas in nota:
            if notas['nota'] == nota:
                print(f"As notas são: {nota}")

    def mostrarMedia(self):
        self.media += self.nota / 3
        if self.media >= 7:
            print("Aluno foi aprovado")
        else:
            print("Aluno foi reprovado")


if __name__ == 'main':
    escola = Escola(nota=7, media=4, nomeAluno='Mateus')
    print(escola)
