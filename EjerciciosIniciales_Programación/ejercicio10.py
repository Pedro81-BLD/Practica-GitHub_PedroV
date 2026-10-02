#Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
variable1= float(input("Introduce un número: "))
variable2= float(input("Introduce otro número: "))

print("El cociente es:", round(variable1 / variable2, 2))
print("El resto es:", variable1 % variable2)
if variable1 % 2 == 0:
    resultado = "par"
else:
    resultado = "impar"

print("El dividendo es", resultado)