class Televisao():

    def __init__(self):
        self.ligada = False
        self.canal = 5

    #Função que faz a condição: se a tv estiver desligada, senão ligue a tv
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    #Verfica se a tv está ligada, se sim , mude para 1 canal 
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

#Instância da classe Televisao
if __name__ == '__main__':
    televisao = Televisao()
    print("Televisão está ligada: {} ". format(televisao.ligada))
    televisao.power()
    print("Televisao está ligada: {} ". format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'. format(televisao.ligada))
    print("Canal: {} ". format(televisao.ligada))
    televisao.power()
    print("Televisão está ligada: {} ". format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.diminui_canal()
    print("Canal: {} ". format(televisao.canal))
    # televisao.diminui_canal()
    # print('Canal: {}'.format(televisao.canal))
