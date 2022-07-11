from pprint import pprint
from re import I
from xml.etree.ElementTree import QName

Suma = 0
Producto = 1
Contador_cero = 0

N = int(input("Ingrese el número de valores de A: "))

for i in range(N):
    dato=int(input("Ingrese el valor de A: "))
    if dato<0:
        Suma=Suma+dato
    elif dato>0:
        Producto=Producto*dato
    else:
        Contador_cero=Contador_cero+1

print("La sumatoria de los valores negativos no nulos es: ", Suma)
print("La productoria de los valores positivos no nulos es: ", Producto)
Porcentaje = Contador_cero / N * 100
print("El porcentaje de valores nulos es: ", Porcentaje, "%")
