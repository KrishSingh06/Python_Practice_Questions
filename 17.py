# polymorphism in python
 # static polymorphism: method overloading
# dynamic polymorphism: method overriding

# class Bank:
#     def __init__(self):
#         self.title = "title"

#     def show(self):
#         print("Title of Bank ",self.title)

# class Edition(Bank):
#     def __init__(self,t,i):
#         super().__init__(t) 
#         self.edi = i

#     def show(self):
#         super().show()
#         print("Edition",self.edi)

# ob1 = Edition("Python","4th")
# ob1.show()

# ob2 = Book ("Java") 
# ob2.show()

# create a class tranport with variables types , 
# Create to child classes boat and Bus with boat has variable capacity, source ,destination 
# bus
# intialize all the variables of all the classes with constructor
# define show method in transport class 
# define show method in boat class to display the record of boat 
# define show method in bus class
# create a 2 object of both of the class 

class Transport:
    def __init__(self, type):
        self.type = type

    def show(self):
        print(f"Type of Transport: {self.type}")


class Waterways(Transport):
    def __init__(self, type, capacity, source, destination):
        super().__init__(type)
        self.capacity = capacity
        self.source = source 
        self.destination = destination

    def show(self):
        super().show()
        print(f"Capacity: {self.capacity}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")


class Roadways(Transport):
    def __init__(self, type, seat_no, source, destination):
        super().__init__(type)
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def show(self):
        super().show()
        print(f"Seat No: {self.seat_no}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")


boat1 = Waterways("Boat", 50, "Goa", "Mumbai")
boat2 = Waterways("Boat", 30, "Kochi", "Alleppey")
 
bus1 = Roadways("Bus", 24, "Delhi", "Jaipur")
bus2 = Roadways("Bus", 40, "Pune", "Nashik")

print("Boat 1:")
boat1.show()

print("\nBoat 2:")
boat2.show()

print("\nBus 1:")
bus1.show()

print("\nBus 2:")
bus2.show()

