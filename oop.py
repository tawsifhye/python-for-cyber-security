class Car:
    def __init__(self, color, make,model):
        self.color = color
        self.make = make
        self.model = model
        self.gas = 0
    
    def getGas(self):
        self.gas+=10

    def checkGas(self):
         return self.gas


car1 = Car('black', 'honda', 'crv')
car2 = Car('black', 'BMW', 'X7')
# print(car1.color, car1.make, car1.model)
# print(car2.color, car2.make, car2.model)

print(car1.checkGas())
car1.getGas()
print(car1.checkGas())