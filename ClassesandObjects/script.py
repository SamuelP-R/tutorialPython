class Myclass:
    variable = "blah" #atributo de la clase 

    def function(self):
        print("Esto es un mensaje dentro de la clase")#metodo de la clase 


myobjectx = Myclass()#se crea una instancia de la clase o el objeto
myobjecty = Myclass()


myobjectx.variable = "locura"

#print(myobjectx.variable)# imprime el atributo 
#print(myobjecty.variable)



myobjectx = Myclass()
myobjectx.function()


class NumberHolder:

    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number

var = NumberHolder(7)
print(var.returnNumber())