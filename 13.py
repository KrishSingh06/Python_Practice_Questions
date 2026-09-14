# # // define a dictionary student where roll no is key and value is another dictionary consisting of name,department,marks of the student. 
# # //perform the lambda function on the dictionary
# 1. Sort the dictionary based on the marks of the student in descending order
# 2. print the record of the student who score max marks
# 3. find the avg marks of the student
# 4. print the records of students who have marks more than avg marks

students = {
    "R1": {"name": "Kanishk", "department": "CSE", "marks": 85},
    "R2": {"name": "Arav", "department": "ECE", "marks": 78},
    "R3": {"name": "Karan Pandey", "department": "CSE", "marks": 92},
    "R4": {"name": "Ibrahim", "department": "ME", "marks": 65},
    "R5": {"name": "Vikash", "department": "ECE", "marks": 88},
    "R6": {"name": "Aman", "department": "CSE", "marks": 75},
    "R7": {"name": "Saswata", "department": "CSE", "marks": 90},
}

sorted_students = dict(sorted(students.items(), key=lambda x: x[1]["marks"], reverse=True))

max_student = max(students.items(), key=lambda x: x[1]["marks"])

print("Student with maximum marks:")
print(max_student[1])


total_marks = sum(student["marks"] for student in students.values())
avg_marks = total_marks / len(students)


above_avg_students = {roll: info for roll, info in students.items() if info["marks"] > avg_marks}
print("\nStudents with marks above average:")
for roll, info in above_avg_students.items():
    print(f"Roll No: {roll}, Name: {info['name']}, Department: {info['department']}, Marks: {info['marks']}")

