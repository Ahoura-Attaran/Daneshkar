class Vehicle():
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.__model = model
        self.year = year
        self.max_speed = speed

    def getmodel(self):
        return (self.__model)
    
    def setmodel(self, model):
        self.__model = model

    def pricing(self):
        return ((self.max_speed * 10) + self.year)
    
    def __str__(self):
        return f"{self.brand} \n {self.year} \n {self.max_speed} \n {self.__model}"
    
    def __eq__(self, value):
        if isinstance(value, Vehicle):
            return (self.brand == value.brand 
                    or self.max_speed == value.max_speed)

class Car(Vehicle):
    def __init__(self, brand, model, year, speed, doors, fuel_type):
        super().__init__(brand, model, year, speed)
        self.doors = doors
        self.fuel = fuel_type

    def __str__(self):
        return (f"{self.brand} \n {self.year} \n {self.max_speed} \n {self.getmodel()}"
                  f"\n {self.doors} \n {self.fuel}")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, speed, engin_cap):
        super().__init__(brand, model, year, speed)
        self.engin = engin_cap

    def __str__(self):
        return (f"{self.brand} \n {self.year} \n {self.max_speed} \n {self.getmodel()}"
                  f"\n {self.engin}")
    
    def pricing(self):
        return (self.engin + (self.max_speed * 5) + self.year)
    
class Bicycle(Vehicle):
    def __init__(self, brand, model, year, speed, size):
        super().__init__(brand, model, year, speed)
        self.size = size

    def __str__(self):
        return (f"{self.brand} \n {self.year} \n {self.max_speed} \n {self.getmodel()}"
                  f"\n {self.size}")
    
