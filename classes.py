class Car:
    """A simple attempt to model a car"""

    def __init__(self, make, year):
        """Initializing make and year attributes."""
        self.make = make
        self.year = year

    def drive_forward(self):
        """simulating a car driving in response to action"""
        print(f"{self.make.title()} is now driving forward.")

    def drive_backward(self):
        """simulating a car driving in response to action."""

        print(f"{self.make.title()} driving backward.")


my_car = Car('Chevy', 2018)

print(f"my car's make is {my_car.make.title()}.")
print(f"my car has been made in {my_car.year}.")
my_car.drive_forward()
my_car.drive_backward()

your_car = Car('lexus', 2004)

print(f"\nyour car's make is {your_car.make.title()}.")
print(f"your car has been made in {your_car.year}.")
your_car.drive_forward()
your_car.drive_backward()

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        """we want the dog listen to our command"""
        print(f"{self.name} is now barking")

    def sit(self):
        """we want out dog to listen to our command"""
        print(f"{self.name} is now sitting")

my_dog = Dog('rex', 11)
dog1 = Dog('bobik', 15)
dog2 = Dog('tuik', 3)
print(f"\nmy dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.")
my_dog.bark()
my_dog.sit()
print(f"\nmy dog's name is {dog1.name}.")
print(f"my dog is {dog1.age} years old.")
dog1.bark()
dog1.sit()
print(f"\nmy dog's name is {dog2.name}.")
print(f"my dog is {dog2.age} years old.")
dog2.bark()
dog2.sit()

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_resaurant(self):
        print(f"this is {self.restaurant_name.title()} restaurant")
        print(f"this is {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"this place open from 10am to 10pm")

place = Restaurant('dushanbe', 'uzbek-cousine')
place1 = Restaurant('nargiz', 'tajik-cuisine')
place2 = Restaurant('afsona', 'samarkand-cuisine')
place3 = Restaurant('tandir', 'isfara-cuisine')

print(f"\nfirst print {place.restaurant_name}")
print(f"second print {place.cuisine_type}")
place.describe_resaurant()
place.open_restaurant()
place1.describe_resaurant()
place2.describe_resaurant()
place3.describe_resaurant()


class Auto:

    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_describe_name(self):
        """return a neatly formated discriptive name"""
        long_name = str(self.year)+ ' ' + self.make.title()+ ' ' +self.model.title()
        return long_name

    def read_odometer(self):
        """Print statement showing car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        set odometer reading to te given value
        Reject the change if it attempts to roll odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_auto = Auto('subaru', 'outback', 2013)
print(my_used_auto.get_describe_name())
my_used_auto.update_odometer(23500)
my_used_auto.read_odometer()
my_used_auto.increment_odometer(100)
my_used_auto.read_odometer()
my_new_auto = Auto('audi', 'a4', '2016')
print(my_new_auto.get_describe_name())
my_new_auto.update_odometer(23)
my_new_auto.read_odometer()


