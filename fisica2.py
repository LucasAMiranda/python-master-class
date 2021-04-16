def determinaPontoChegada():
  pi = float(input("Informe a posição inicial: "))
  v = float(input("Informe a velocidade : "))
  deltaT = float(input("Informe o tempo Inicial: "))

  s = pi  + v * deltaT
  print(s)


pf = determinaPontoChegada()
print(pf)