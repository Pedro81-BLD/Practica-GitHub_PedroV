#Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
peso = float(input("Introduce tu peso corporal en kg: "))
altura = float(input("Introduce tu altura en m: "))
imc = float(round(peso / (altura ** 2),2))

if imc > 25:
    print("Si tu peso es", peso, "y tu altura es", altura, "tu IMC es:", imc,". Hay sobrepeso.")
else:
    print("Si tu peso es", peso, "y tu altura es", altura, "tu IMC es:", imc)