
class Animal:
    def sound(self):
        return "Animal makes a sound"

class Dog(Animal):
    def sound(self):
        return "Dog barks"

class Cat(Animal):
    def sound(self):
        return "Cat meows"

print("Method overriding")

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())
