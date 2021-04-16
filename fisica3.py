def robo():
  si = float(input("Informe a posição inicial de um robô: "))
  v = float(input("Informe a velocidade : "))
  deltaT = float(input("Informe o tempo Inicial: "))

  tf = si  + v * deltaT
  print(tf)

#exibi a posição final de um robô em relação ao tempo
pf = robo()
print(pf)