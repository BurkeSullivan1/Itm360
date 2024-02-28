"""
Hidden attributes are, only accessible in the class and hidden from the user for
privacy.
To access any hidden attributes from outside the class, have to call the respective
methods.
"""
class Car:
    def __init__(self,make,model,year): # car class, with three hidden data attributes: make, model, year
        self.__make=make
        self.__model=model
        self.__year=year
        self.odometer_reading = 0 #set a default value for an attribute
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year=year
    def __str__(self): # _str_ method displays the state (value) of the object; it is always executed when the class is called.
        return 'make: ' + self.__make + '\nmodel: ' + self.__model + '\nyear: ' + self.__year
    def car_instance():
        my_new_car = Car('audi', 'a4', 2024)
    #print(f"My new car is {my_new_car.__year} {my_new_car.__make}{my_new_car.__model}")
    print(f"My new car is {my_new_car.get_year()} {my_new_car.get_make().title()}{my_new_car.get_model().title()}")
    #To Update a Value of a hidden attribute, have to update through its encapsulatedmethod
def update_car():
    my_new_car = Car('audi', 'a4', 2024)
my_new_car.set_year('2013')
print(f"My new car is {my_new_car.get_year()} {my_new_car.get_make().title()}
{my_new_car.get_model().title()}")
#To update a regular attribute, a direct re-assignment works as well
my_new_car.odometer_reading = 100000
print(f"The mileage of this car is {my_new_car.odometer_reading}")
