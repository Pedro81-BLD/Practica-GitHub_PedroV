#Una tienda aplica un 21% de descuento a un producto y después añade un 21% de IVA.
var_precio=float(input("Introduce el precio de la entrada : "))

calculo=var_precio - (var_precio*0.1)

print("El precio de la entrada con descuento es:", calculo)
print("El precio de la entrada con descuento e IVA es:", calculo + (calculo*0.21))