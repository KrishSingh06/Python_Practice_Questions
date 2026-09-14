# write a program in python to take a year and find out whether is a year leap year or not

year = int(input("Enter the year to check leap year or not :"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
