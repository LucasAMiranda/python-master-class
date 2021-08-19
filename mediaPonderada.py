nota1 = float(input("Nota 1:"))
peso1 = float(input("Peso 1:"))
 
nota2 = float(input("Nota 2:"))
peso2 = float(input("Peso 2:"))
 
mediaPond = (nota1*peso1 + nota2*peso2) / (peso1+peso2)
 

print(f"Média: {mediaPond:.2f}")