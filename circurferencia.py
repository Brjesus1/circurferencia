# Importar la biblioteca math
import math

# Definir la constante pi con 6 decimales
pi = round(math.pi, 6)

# Definir los radios
radio1= 3
radio2= 8
radio3= 10

# Calcular las circunferencias
circunferencia1 = round(2 * pi * radio1, 6)
circunferencia2 = round(2 * pi * radio2, 6)
circunferencia3 = round(2 * pi * radio3, 6)

# Imprimir los resultados
print("La circunferencia del círculo con radio", radio1, "es:", circunferencia1)
print("La circunferencia del círculo con radio", radio2, "es:", circunferencia2)
print("La circunferencia del círculo con radio", radio3, "es:", circunferencia3)

