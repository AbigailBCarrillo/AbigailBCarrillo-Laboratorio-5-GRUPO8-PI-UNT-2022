print('Secuencia de Tribonacci'.upper()) #TITULO
print('Se define el valor de Tn para todo n empezando desde 0')
def tribonacci(n): #DEFINIENDO LA FUNCION
    if n < 1 :
        return 0
    if 0<n<3:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci (n-3)

n=int(input('Escriba valor de "n" en para hallar el Tn en la secuencia de Tribonacci: '))
print('El Tn de la serie de Tribonacci es {}'.format(tribonacci(n)))#RESULTADO