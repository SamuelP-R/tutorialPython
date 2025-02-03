"""
Bucles(lops) hay dos tipos de bucles en python, for y while
El bucle for 
"""
primes = [2,3,5,7,8]
# in es un operador muy util que se utiliza para verificar si un elemento esta presente dentro de una secuencia, como una lista, una cadena, una tupla o un diccionario
for prime in primes:
    print(prime)

print("out the numbers 0,1,2,3,4")
for x in range(5):
    print(x)

print("out 3,4,5")
for x in range(3,6):
    print(x)

print("out 3,5,7")
# es en el rango del 3 al 8, se le suma dos, queda 5 se le suma 2 queda 7  se suma otros es 9 pero ya no se imprime porque ya sale del rango que es hasta el 8
for x in range(3,8,2):
    print(x)

#while loops
print("while loops")

count = 0
while count < 5:
    print(count)
    count += 1

print ("out 0,1,2,3,4")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# prints out only odd numbers -1, 3,5,7,9
for x in range(10):#itera desde 0 hasta 9
    #verifica si x es un numero par
    if x % 2 == 0:
        continue#salta la iteracion y pasa al siguiente numero
    print(x)