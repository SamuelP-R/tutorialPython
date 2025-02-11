phonebook = {}
phonebook["Mane"] = 77972838828
phonebook["Antonio"] = 73674732834848
phonebook["Fer"] = 747384729729
print(phonebook)

#Otra Alternativa
phonebooks = {
    "Samuel" : 982992929293,
    "Isa" : 93283828282,
    "Johan" : 929292832
}

print(phonebooks)


numerotelefono = {
    "Samuel" : 982992929293,
    "Isa" : 93283828282,
    "Johan" : 929292832
}
for name, number in numerotelefono.items():
    print("Numero de telefono de %s es %d" % (name, number))

#Eliminar un valor
del numerotelefono["Johan"]
print(numerotelefono)