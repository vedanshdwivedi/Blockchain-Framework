import vehicle

class Bus(vehicle.Vehicle):
    # __passengers = []

    def __init__(self, speed=100):
        super().__init__(speed)
        self.__passengers = []

    def add_passenger(self, passenger):
        self.__passengers.append(passenger)
    
        

bus1 = Bus(150)
bus1.drive()
name = input('Sawari ka naam kya hai be ??')
bus1.add_passenger(name)
bus1.add_warning('Laitrine h Passenger')
bus1.show_warnings()
'''
car2 = Car(200)
car2.drive()

car3 = Car(250)
car3.drive()'''
