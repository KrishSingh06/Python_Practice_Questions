# wap in python find out name of student who have marks maximum and minimum marks from the list of student names and marks. do not take duplicate names and marks in the list.
# the list are unsorted

student_names = ["Kanishk", "Brajesh", "Sagar", "David", "Arya", "Karan", "Suman", "Henry", "Ivy", "Jack"]
student_marks = [60, 45, 78, 55, 88, 40, 92, 67, 73, 59]


unique_students = list(set(student_names))
unique_marks = list(set(student_marks))

max_marks = max(unique_marks)
min_marks = min(unique_marks)

max_mark_index = student_marks.index(max_marks)
min_mark_index = student_marks.index(min_marks)

max_student = student_names[max_mark_index]
min_student = student_names[min_mark_index]

print("Student with maximum marks:", max_student)
print("Student with minimum marks:", min_student)