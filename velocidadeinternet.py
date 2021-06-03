#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

link = "https://github.com/LucasAMiranda/"

with open("testevelocidade.txt", "w") as arquivo:
    tamanho = int(input("O tamanho do arquivo para download (MB): "))
    conteudo = arquivo.write(str(tamanho))
    velocidade = int(input("velocidade do link (Mbps): "))
    conteudo = arquivo.write(str(velocidade))


with open("testevelocidade.txt", "w") as arquivo:
    tempo = int(input("O tempo aproximado de download: "))
    conteudo = arquivo.write(str(tempo))
    minutos = (tempo + velocidade)/60
    conteudo = arquivo.write(str(minutos))
    print("O tempo aproximado usando o link ", link, " foi de ", minutos, " minutos")

with open("testevelocidade.txt", "w") as arquivo:
    arquivo.write(str(conteudo))
