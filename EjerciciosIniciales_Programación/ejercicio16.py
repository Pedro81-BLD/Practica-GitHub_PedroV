# Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos  resultados de todo el proceso (raíz y división).
import math
variable1 = int(input("Introduce un número: "))

print("El resultado de la raíz es:", round(math.sqrt(variable1), 1))
print("El resultado de la división es:", math.sqrt(variable1) // 2)