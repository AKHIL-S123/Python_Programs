class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} {self} years old.")


    def display(self):
        print(self)
# Create a Person object
person = Person("Alice", 25)
#

# Access attributes and call methods
print(person.name)   # Output: "Alice"
print(person.age)    # Output: 25
person.introduce()   # Output: "Hello, my name is Alice and I am 25 years old."
person.di