print('Programa para ordenar promedios de alumnos'.upper())
print(' ')
matriz = []
N=int(input('¿Cuántos niños hay? '))

for x in range(N):
    matriz.append([0]*2) #CREANDO LA MATRIZ

for y in range (N):
    matriz[y][0]=str(input('Ingrese el nombre del {}° alumno: '.format(y+1)))
    matriz[y][1]=float(input('Ingresa el promedio de {}: '.format(matriz[y][0]))) #DANDO VALORES A LA MATRIZ

print('Usted a ingresado estos datos:')
print(' ')
print('ALUMNO  NOTA')
for c in range(N):
    print(matriz[c][0],end=(' '))
    print(matriz[c][1])
print(' ')
numeros=[]
for a in range(N):
    numeros.append(matriz[a][1]) 

numeros.sort() #ORDENANDO LOS NUMEROS
print('Los datos ordenados:')
print(' ')
print('ALUMNO  NOTA')

for z in range(N):
    b=0
    while matriz[b][1] != numeros[z]:
        b=b+1
    if matriz[b][1] == numeros[z]:
        print(matriz[b][0],end=(' '))
        print(matriz[b][1])
#CUADRO CON NOTAS DE ALUMNOS