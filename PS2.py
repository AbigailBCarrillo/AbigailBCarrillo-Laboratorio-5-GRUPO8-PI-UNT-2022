from cmath import sqrt

X1 = []
X2 = []
promedio = []
media_geo = []

valor = 0
print("Ingrese el número de pares de valores: ")
tamaño = input()
tamaño = int(tamaño)
while tamaño<=0:
    print("Ese no es un número válido, pruebe otra vez: ")
    tamaño = input()
    tamaño = int(tamaño)

i=0
while i < tamaño:
    print("Ingrese el número ", 1, " del par de valores número ", i+1, " (debe ser un valor positivo no nulo):")
    valor = input()
    valor = float(valor)
    while valor <= 0: 
        print("El valor ingresado no es un valor positivo no nulo. Pruebe otra vez: ")
        valor = input()
        valor = float(valor)
    X1.append(valor)
    print("Ingrese el número ", 2, " del par de valores número ", i+1, " (debe ser un valor positivo no nulo):")
    valor = input()
    valor = float(valor)
    while valor<=0: 
        print("El valor ingresado no es un valor positivo no nulo. Pruebe otra vez: ")
        valor = input()
        valor = float(valor)
    X2.append(valor)
    i+=1

i=0
j=0 #cuenta el número de veces en que el promedio es menor que la media geométrica
while i<tamaño:
    promedio.append((X1[i]+X2[i])/2)
    print("El promedio de los números ", X1[i], " y ", X2[i], " es: ", promedio[i])
    media_geo.append((X1[i]*X2[i])**0.5)
    print("La media geométrica de los números ", X1[i], " y ", X2[i], " es: ", media_geo[i])
    if promedio[i] < media_geo[i]: j = j+1
    i+=1

i=tamaño-1
k=-1 #índice de la lista en la que el promedio es igual a la media geométrica por primera vez
while i>=0:
    if promedio[i] == media_geo[i]: 
        k=i
    i-=1

print("El promedio ha sido menor que la media geométrica el ", abs(100*j/i), "%", " de las veces.")

if k == -1:
    print("En ningún par de valores se cumple que el promedio sea igual a la media geométrica.")
else: print("El primer par de valores en la lista cuyo promedio es igual a su media geométrica es", X1[k], "y", X2[k], "(el par de valores número", k+1, ", hallado en el índice número", k, ").")