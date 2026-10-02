# Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math
diámetro = float(input("Introduce el diámetro del círculo: "))

print("El perímetro del circulo es:", round(diámetro * math.pi, 1))
print("El área del círculo es:", round(math.pi * ((diámetro / 2) ** 2), 1))