
class Car:
    def move(self):
        return "Car is driving"

class Boat:
    def move(self):
        return "Boat is sailing"

def start_moving(vehicle):
    print(vehicle.move())

print("Duck typing")

start_moving(Car())
start_moving(Boat())
