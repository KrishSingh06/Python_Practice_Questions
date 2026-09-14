# wap in python to create a list of 10 student names. create another list which having the marks of 10 students and print the names of students who have marks greater than 50.
student_names = ["Kanishk", "Brajesh", "Sagar", "David", "Arya", "Karan", "Suman", "Henry", "Ivy", "Jack"]
student_marks = [60, 45, 78, 55, 88, 40, 92, 67, 73, 59]

passed_students = []

for i in range(len(student_names)):
    if student_marks[i] > 50:
        passed_students.append(student_names[i])

# Print the new list
print("Students with marks greater than 50:")
print(passed_students)