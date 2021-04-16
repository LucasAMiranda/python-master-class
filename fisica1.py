def Tempo():
  i = int(input("Informe o horário Inicial mm:ss: "))

  f = int(input("Informe o horário final em mm:ss: "))

  deltaT  = i - f;

  print(f"O tempo é {i}: {f}".format(deltaT))

Tempo()
