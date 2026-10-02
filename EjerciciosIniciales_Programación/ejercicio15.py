#Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))

print("El área del cilindro es:", round(((math.pi * (radio ** 2)) * 2) + ((radio * 2) * math.pi * altura), 2))
print("El volumen del cilindro es:", round(math.pi * (radio ** 2) * altura, 2))