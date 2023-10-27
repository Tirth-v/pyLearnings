from OOP.Abstraction.abstract_class import Vehicle
class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color = color

    def start(self):
        print("Kick start")


class Moped(Vehicle):
    def __init__(self,n):
        super().__init__(self,n)

    def start(self):
        print("Self start")


class Car(Vehicle):
    def __init__(self,n,gears):
        super().__init__(self,n)
        self.no_of_gears = 6

    def start(self):
        print("Key start")

