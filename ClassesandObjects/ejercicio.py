"""Ejercicio
Tenemos una clase definida para vehículos. Crea dos nuevos vehículos llamados car1 y car2. Establezca el car1 como un convertible rojo con un valor de $ 60,000.00 con el nombre de Fer, y car2 para ser una camioneta azul llamada Jump con un valor de $10,000.00."""
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())