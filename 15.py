# create a class Student with attributes name ,dept,roll,intialize the attributes with Constructor.
# Display the record of Student using show().
# define 5 Student objects and show records of 5 students

class Student:
    def __init__(self, name, dept, roll):
        self.name = name
        self.dept = dept
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}, Department: {self.dept}, Roll No: {self.roll}")

student2 = Student("Bobby", "Mathematics", 2)
student3 = Student("Chandan", "Physics", 3)
student4 = Student("Karan", "Chemistry", 4)
student5 = Student("Khushi", "Biology", 5)

student1.show()
student2.show()
student3.show()
student4.show()
student5.show()