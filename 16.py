# class super:
#     def display(self):
#         print(" super ")

# class sub(super):
#     def display(self):
#         print(" sub ")
# ob1 = sub()
# ob1.display()
# ob1.show()

class Student:
    def __init__(self,roll,name):   

        self.roll = roll
        self.name = name
    
class ugstudent(Student):
    def __init__(self,roll,name):
        super().__init__(roll,name)
        self.idp = "UG"

    def show(self):
        print(self.roll)
    

# crete a class tranport with a method get val() to intialize the variable type (tranport).
# Define to method show().
# Create a child class bus with the method input val() to intialize the variable the variable seat number ,source , destination.
#  Define a method display to show all the variable of the bus .
# Initialize the variable class transport and bus with constructor

class Transport:
    def __init__(self):
        self.transport_type = None

    def get_val(self, transport_type):
        self.transport_type = transport_type

    def show(self):
        print(f"Transport Type: {self.transport_type}")


class Roadways(Transport):
    def __init__(self):
        super().__init__()
        self.seat_number = None
        self.source = None
        self.destination = None
    
    def input_val(self, seat_number, source, destination):
        self.seat_number = seat_number
        self.source = source
        self.destination = destination

    def display(self):
        self.show()
        print(f"Seat Number: {self.seat_number}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")

obj1 = Roadways()

obj1.get_val("Roadways")
obj1.input_val(25, "Kolkata", "Durgapur")

# Display all values
obj1.display()

# Initialize the variable class transport and bus with constructor
transport = Transport()
bus = Roadways()
