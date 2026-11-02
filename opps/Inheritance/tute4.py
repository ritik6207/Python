# MutiLevel Inheritance
# Base class
class Network:
    def connectivity(self):
        return "Network connects"

# Derived class
class Network_5G(Network):
    def fast_connectivity(self):
        return "5G Network provides superfast connectivity"

    def connectivity(self):
        return "5G Network connects faster"

# Sub-derived class
class Network_5G_Airtel(Network_5G):
    def fast_and_stable_connectivity(self):
        return "Airtel 5G network is fast and remains stable"

# Creating an instance of Network_5G_Airtel
obj1 = Network_5G_Airtel()
print(obj1.connectivity())  # Inherited from Network class


# Overriding
# Base class
class Vehicle:
    def start(self):
        return "Vehicle starts"

# Derived class
class Car(Vehicle):
    def start(self):
        return "Car starts"

# Sub-derived class
class SportsCar(Car):
    def start(self):
        return "Sports Car starts"

# Creating an instance of SportsCar
sports_car = SportsCar()
print(sports_car.start())  # Calls the start method of SportsCar class