
#create a 2d array to store the marks of 3 subject  of student marks perform the following operation on the marks array 

import numpy as np
marks = np.array([
    [78, 85, 90],
    [88, 76, 95],
    [92, 89, 84],
    [65, 43, 70],
    [81, 94, 88],
    [75, 80, 91]])

print("Marks Array:")
print(marks)

# 1. Find the maximum marks
print("\nMaximum marks:", np.max(marks))

# 2. Find the minimum marks
print("Minimum marks:", np.min(marks))

# 3. Find the average marks
print("Average marks:", np.mean(marks))

# 4. Find the student ID (0 to 5) who scored maximum marks in Subject 1
student_id = np.argmax(marks[:, 1])
print("Student ID who scored maximum marks in Subject 1:", student_id)
print("Maximum marks in Subject 1:", marks[student_id, 1])

# 5. Find maximum marks subject-wise
max_subject_wise = np.max(marks, axis=0)
print("Maximum marks subject-wise:", max_subject_wise)

# 6. Find average marks subject-wise
avg_subject_wise = np.mean(marks, axis=0)
print("Average marks subject-wise:", avg_subject_wise)

# 7. Add 10 marks for all students who score less than 50 in Subject 1
marks[marks[:, 1] < 50, 1] += 10

print("After adding 10 marks in Subject 2:")
print(marks)

#8. Find number of students who score more than 80 in Subject 2
count = np.sum(marks[:, 2] > 80)
print("Number of students scoring more than 80 in Subject 2:", count)


# 9. Find minimum marks of Student 2
min_student_2 = np.min(marks[1])
print("Minimum marks of Student 2:", min_student_2)


# 10. Find maximum marks of Student 4
max_student_4 = np.max(marks[3])
print("Maximum marks of Student 4:", max_student_4)