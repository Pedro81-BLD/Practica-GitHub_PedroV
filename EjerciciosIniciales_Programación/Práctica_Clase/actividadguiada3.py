#calcular longitud y área de un círculo
import math
radio=float(input("Introduce el radio del círculo: "))

area=math.pi*(radio**2)
longitud=math.pi*2*radio

print(f"El área del círculo es: {area:.2}")
print(f"La longitud del círculo es: {longitud:.2}")


#otra manera de hacer el ejercicio
import math

radio=float(input("Introduce el radio: "))
