
def fatorial(x):
  fat = 1
  cont = 1  
  while cont <= x:
    fat *= cont #isso é o mesmo que fat = fat * cont
    cont += 1 #isso é o mesmo que cont = cont + 1
  return(fat)
