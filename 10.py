# create a tuple of 20 employee name and perform the following operation on the tuple
from shutil import move


employees = ("Alice", "Bob", "Krish", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Kanishka", 
             "Rohan", "Sohan", "Krish", "Aditya", "Riya", "Siya", "Rinkesh", "Sonu", "Monu", "Jeet")

#print each name and no of frequency in list 
for name in employees:
    print(f"{name}: {employees.count(name)}")
employee_list=list(employees)


# wap to remove the duplicate name from the tuple and find the distinct name in the tuple
employee_set = set(employees)   
i = 0
while i < len(employee_list):
    current_name = employee_list[i]
    if current_name in employee_list[:i]:
        employee_list.remove(current_name)
    else:   
        i += 1          
distinct_employees = tuple(employee_set)
print("Distinct employee names:", distinct_employees)

# wap to print the name of the employee having max frequency in the tuple
max_frequency = 0
max_name = ""
for name in distinct_employees:
    frequency = employees.count(name)
    if frequency > max_frequency:
        max_frequency = frequency
        max_name = name
print(f"Employee with maximum frequency: {max_name} (Frequency: {max_frequency})")


# sort tuple in alphabetical order and print the sorted tuple
sorted_employees = sorted(distinct_employees)
print("Sorted employees:", sorted_employees)


# input a specific emp name and find whether the name exist in the tuple or not
specific_name = input("Enter an employee name to search: ")
if specific_name in distinct_employees:
    print(f"{specific_name} exists in the tuple.")
else:
    print(f"{specific_name} does not exist in the tuple.")