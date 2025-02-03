astring = "Hello World!"
astring2 = 'Hellor World!'

print("single quotes are ''")

print(len(astring))


print(astring.index("o"))
print(astring.count("l"))

print(astring[3:7])
print(astring[3:7:2])
print(astring[3:7])
print(astring[3:7:1])
print(astring[::-1])

#convertir a mayusculas o minusculas
print(astring.upper()) #mayusculas
print(astring.lower()) #minusculas

#determina si la cadena comienza con algo o termina con algo
print(astring.startswith("Hello"))
print(astring.endswith("siuuuu"))

#divide la cadena
affewword = astring.split(" ")