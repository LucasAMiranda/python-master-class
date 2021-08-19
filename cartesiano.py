from math import sqrt

# Inserido coordenadas dos pontos
xA = float(input('Digite a abscissa do ponto A:'))
xB = float(input('Digite a abscissa do ponto B:'))

yA = float(input('Digite a ordenada do ponto A:'))
yB = float(input('Digite a abscissa do ponto B:'))

# Calculando a distância
distAB = sqrt((xA-xB)**2) + ((yA-yB)**2)

# Mostrando resultado
print('A distância entre esses dois pontos é de:', distAB, 'unidades de medida')