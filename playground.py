# *args: Many Positional Arguments 

def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)
    

add(3,5,7,9,200,700,1000,1,1,1,1,1,1,1,1)

# **kwargs: Many Keyword Arguments

def calculate(n, **kwargs):
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(3, add = 3, multiply = 5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")#we use .get in dictionaries incase the key dos not exist so it will return none

my_car = Car(make= "Nissan")
print(my_car.model)