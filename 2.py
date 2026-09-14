# write a program for calculator for 2 no      and perform following operation : Addition, Subtraction, Multiplication, Division

a = float(input("Enter the first no:"))
b = float(input("Enter the second no:"))

def calculator(a,b):
    switch = input("Enter the operations you want to perform: +, -, *, / : ")

    if switch == "+":
        print("Addition of two no is : ",a+b)
    elif switch == "-":
        print ("Subtraction of two bo is :",a-b)
    elif switch == "*":
        print("Multiplication of two no is :",a*b)
    elif switch == "/":
        if b == 0:
            print("Division by zero is not allowed.")
        else:
            print("Division of two no is :",a/b)
    else:
        print("Invalid operation selected.")

calculator(a,b) 

