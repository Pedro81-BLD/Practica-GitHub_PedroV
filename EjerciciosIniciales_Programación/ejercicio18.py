#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
num_adultos = int(input("Introduce el número de adultos: "))
num_menores = int(input("Introduce el número de menores: "))

print("El precio total para", num_menores, "menor/es es:", round((12 -((12 * 50) / 100)) * num_menores, 1))
print("El precio total para", num_adultos, "adulto/s es:", round((12-((12 * 10) / 100)) * num_adultos, 1))