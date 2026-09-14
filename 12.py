# // Create a dictionary of employee where employee id is key and value is against the employee id is another dictionary which contains empname, empdesignation, department, empsalary.
# // dictionary contains of information 500 employess
# // Now perform the following operation on this dictionary
# // 1. print the name of employee whose employee id is E1
# // 2. print the department of employee whose employee id is E4
# // 3. print the salary of employee whose employee id having maximum salary
# // 4. insert a new employee in the existing dictionary 


employee = {
    "E1": {"name": "Raj", "age": 30, "salary": 50000, "designation": "Manager", "dept": "HR"},
    "E2": {"name": "Sonu", "age": 25, "salary": 40000, "designation": "Developer", "dept": "IT"},
    "E3": {"name": "Kanishk", "age": 35, "salary": 60000, "designation": "Analyst", "dept": "Finance"},
    "E4": {"name": "Dev", "age": 28, "salary": 45000, "designation": "Designer", "dept": "Marketing"},
    "E5": {"name": "Ramu", "age": 32, "salary": 55000, "designation": "Consultant", "dept": "Operations"}
}

emp_id = "E1"
print("Details of E1:", employee[emp_id])

emp_id = "E4"
print("Department of E4:", employee[emp_id]["dept"])

max_salary = employee["E1"]["salary"]
max_emp = "E1"

for emp in employee:
    if employee[emp]["salary"] > max_salary:
        max_salary = employee[emp]["salary"]
        max_emp = emp

print("Employee with highest salary:")
print(employee[max_emp])

employee["E6"] = {
    "name": "Anita",
    "age": 29,
    "salary": 48000,
    "designation": "HR Executive",
    "dept": "HR"
}

print("Employee record added successfully.")
print(employee)