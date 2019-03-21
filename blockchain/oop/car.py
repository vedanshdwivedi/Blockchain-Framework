from vehicle import Vehicle

class Car(Vehicle):
    def brag(self):
        print('Ye duniya pittal di, baby doll me sone di....')
    
        

car1 = Car()
car1.drive()
car1.warnings.append('Bas aise hi checking')
print(car1)
'''
car2 = Car(200)
car2.drive()

car3 = Car(250)
car3.drive()'''
