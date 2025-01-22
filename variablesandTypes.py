#Numbers
#Define an integer
myint = 4
print(myint)

#Define a floating point numer
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
#float(7) convierte el  numero entero a tipo flotante
myfloat = float(myint)
print(myfloat)

#Strings
mystring = 'hello'
print(mystring)
mystring = 'world'
print(mystring)

#Inclusion de apostrofes
mystring = "Dont' worry about apostrophes"
print(mystring)

# Las operaciones poeden ser ejecutadas en numeros y strings
one = 1
two = 2
three = one + two
print(three)

hello ="hello"
world = "world" 
helloWorld = hello + ", " + world
print(helloWorld)

#Variables simultaneas son las que se pueden realizar en la misma linea 
a, b = 3, 4
print(a,b)

# Ejercicio 
mystring = None
myint = None
myfloat = None

if mystring == "hello":
    print("String: %s"  % mystring)
# %s es un especificador de formato que indica que el valor
# que se insertara en esa posicion debe ser tratado como una
#cadena (string)

# el operador % se utiliza para indiacar que lo que sigue
# (despues del %) son los valores que se insertaran en los
# especificadores de formato dentro de la cadena
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)

if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)