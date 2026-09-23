# 1. wap a program to create a series of marks of 5 students 

import pandas as p

marks = p.Series([85, 78, 92, 67, 88],
                  index=["Student 1", "Student 2", "Student 3", "Student 4", "Student 5"])

print(marks)

# wap series of 10 grocery product with their prices .andperform the following on the series
# 1. print the product name & price
# 2 .find the avg price of the product in series
# 3. whose price more than avg price
# 4 .list the products whose price more than 50 rupees

import pandas as pd

products = pd.Series({
    "Rice": 60,
    "Wheat": 45,
    "Sugar": 50,
    "Milk": 30,
    "Oil": 120,
    "Dal": 80,
    "Salt": 20,
    "Bread": 40,
    "Tea": 70,
    "Biscuits": 55
})

print(products)

avg = products.mean()
print("\nAverage Price:", avg)

print("\nProducts whose price is more than average:")
print(products[products > avg])

print("\nProducts whose price is more than 50:")
print(products[products > 50])