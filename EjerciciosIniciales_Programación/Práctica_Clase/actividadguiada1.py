var_grados=int(input("Introduce los grados: "))
'''F=Cx5/9+32'''

calculo=var_grados * 5/9 +32
print("Temperatura:" ,calculo, "ºF")

#otra manera de dar la información con print

print(f"2ª manera de presentar Temperatura: {calculo} F")

#primer método de redondeo
print(round(calculo, 2))
print(f"{calculo:.2f}")