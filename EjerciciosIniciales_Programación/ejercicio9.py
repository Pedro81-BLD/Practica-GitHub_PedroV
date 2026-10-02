#Programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
variable1 = int(input("Introduce un número de segundos: "))

print("El número de minutos es:", variable1 / 60, "y en horas es:", round(variable1 / 60 / 60, 2))