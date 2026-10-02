# Programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?
variable1 = int(input("Introduce un número entero: "))
variable2 = int(input("Introduce otro número entero: "))

print("La suma de ambos números es:", variable1 + variable2)
print("La resta de ambos números es:", variable1 - variable2)
print("El  producto de ambos números es:", variable1 * variable2)
print("La división de ambos números es: ", round(variable1 / variable2, 2))
print("La división entera de ambos números es: ", variable1 // variable2)
print("El resto de ambos números es: ", variable1 % variable2)
print("La potencia de ambos números es: ", variable1 ** variable2)