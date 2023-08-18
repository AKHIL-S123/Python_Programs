class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print(f"\ncar's make year :{self.make} \ncar's model year :{self.model}\ncar's year :{self.year}")

class Electric_car(Car):
    def __init__(self,make,model,year,battery_capacity):
        super().__init__(make,model,year)
        self.battery_capacity =battery_capacity
    def display2(self):
        super().display()
        print(f"Electric car capacity: {self.battery_capacity}")

make=input("Enter cars make :")
model=input("Enter car model :")
year=input("Enter car year :")
battery_capacity=input("Enter battery capacity")
c=Electric_car(make,model,year,battery_capacity)
c.display2()



