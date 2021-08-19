def nota():
  n1 = float(input("Informe a nota1: "))

  ap1 = (n1 * 40)/ 100

  n2 = float(input("Informe a nota2: "))
  ap2 = (n2 * 40) / 100
  
  n3 = float(input("Informe a nota3: "))
  ap3 = (n3 * 20)/ 100

  notaFinal = (n1 + n2 + n3) / (ap1 + ap2 + ap3)

  print(f"A nota final {notaFinal:.2f}")

nota()