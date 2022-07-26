#FIRST EXERCISE:
# class Vehicle:
#     def headlights(self):
#         print("Has 1 headlights")
#
# class Car():
#     def taking_corner(self):
#         print("Doesn't lean in corners")
#
# class Bike(Car):
#     def taking_corner2(self):
#         print("Leans in corners")
#
# class Slingshoot(Bike, Car, Vehicle):
#         pass
#
# slingshoot = Slingshoot()
# slingshoot.headlights()
# slingshoot.taking_corner()



#SECOND EXERCISE:

class Computer(object):
    def typing(self):
        print("It is typing...")
    def clicking(self):
        print("It is clicking...")
    def pixeling(self):                 #in minus la Server
        print("It is pixeling...")
    def __init__(self, central_unit):
        self.central_unit = central_unit


class Laptop(Computer):
    def __init__(self):
        super().__init__("Tablet")


class Server(Computer):
    def __init__(self):
        delattr(super(), "pixeling")

computer=Computer("Unitate Centrala")
laptop=Laptop()
print(laptop.central_unit)
server=Server()

computer.pixeling()
laptop.pixeling()
server.pixeling()
