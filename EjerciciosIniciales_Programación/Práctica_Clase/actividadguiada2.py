#Una tienda aplica un 21% de descuento a un producto y después añade un 21% de IVA.
var_precio=float(input("Introduce el precio de la entrada : "))

calculo=round(var_precio * 0.9 * 1.21, 2)

print("El precio es:", calculo)

#dos formas de printear
print(f"El precio de la entrada con descuento es: {calculo:.2}")
print(f"El precio de la entrada con descuento e IVA es: {calculo + (calculo*0.21):.2}")