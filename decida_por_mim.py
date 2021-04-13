import random 

import  random

def DecidaPorMim():
      respostas = [
          'Sim concordo',
          'Não sei vou pensar',
          'Tenho que estudar mais',
          'vou me organizar nos estudos'
      ]

      input('informe sua pergunta aqui: ')
      print(random.choice(respostas))

DecidaPorMim()

'''
class DecidaPorMim():
    def  __init__(self):
        self.respostas = [
            'Não  sei',
            'Não indico por causa das condiçções favoráveis do tempo',
            'Não vá está muito tarde, perigoso demais!',
            'SIM VAI LÁ ,  na fé'
        ]
 
    def Perguntas(self):
        input('informe aqui sua pergunta: ')
        print(random.choice(self.respostas))


decida = DecidaPorMim()
decida.Perguntas()
'''

'''
def DecidaPorMim(self):
    self.respostas = [
        'Sim concordo',
        'Não sei vou pensar',
        'Tenho que estudar mais',
        'vou me organizar nos estudos'
    ]

def Perguntas(self):
    input('informe sua pergunta aqui: ')
    print(random.choice(self.respostas))


decida = DecidaPorMim('sim vai lá!')
decida.Perguntas()
'''