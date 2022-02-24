#primer metodo
import math
x=float (input("Ingrrese el valor x:"))
n = int (input("Ingrese el valor de n: "))
def funcion_exponencial(x):
    suma = 0

    for n in range(0, 50):
        suma += math.pow(x, n) / math.factorial(n)

    return suma


print('Resultado con la función funcion_exponencial:', funcion_exponencial(2))
print('Resultado con la función math.exp:', math.exp(2))

#Segundo metodo
x=int (input("Ingrese potencia e:"))
n = int (input("Ingrese el valor de n:"))
fact=1
i=1
acum=0

while(i<=n):
    fact=fact*i
    elevar = pow (x,i)
    suma = (elevar + fact)
    acum+=suma
    i=i+1
print ("Valor de la factorial es", 1/acum+1)

