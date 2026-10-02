# Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
base_mayor = int(input("Introduce la base grande del trapecio: "))
base_menor = int(input("Introduce la base pequeña del trapecio: "))
altura = int(input("Introduce la altura del trapecio: "))
lado = int(input("Introduce el lado del trapecio: "))

print("El perímetro del trapecio isósceles es:", base_mayor + base_menor + 2 * lado)
print("El área del trapecio isósceles es:", (base_mayor + base_menor) * altura / 2)