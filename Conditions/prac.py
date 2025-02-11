x = 2
print(x == 2)#prints out true
print(x == 3)#print out false
print(x < 3)#print out true

#Boolenan operators
name = "John"
age = 23
if name =="John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick")

# The in operator
if  name in ["John", "Rick"]:
    print("Your name is either John or Rick")

#Here is an example for using Python's "if" statement using code blocks:
if x == 2:
    print("x equals two")
else:
    print("x does not equal to two")

"The is operator"
a = [1,2,3]
b = [1,2,3]

print(a == b)# true los valores son iguales
print(a is b)# false no son el mismo objeto en memoria 

#The not operator
print("The not operator")
print(not False) #prints out true
print ((not False) == (False))#prints out false


