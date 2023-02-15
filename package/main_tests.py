#Importación de la libreria
from RB import RB

#Input de la red 
input = "./Input/red_3.txt"

#Utilizacion de clase de Red de Bayes
red = RB(input)

#Impresion de resultados
print('P(B): ',red.P('B'))