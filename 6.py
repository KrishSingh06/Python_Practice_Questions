# wap in python to define a method dosum with parameter num to find out the sum of the digit of num and return it 


# def dosum(num):
#     digit_sum = 0
#     while num > 0:
#         digit_sum += num % 10
#         num //= 10
#     return digit_sum

# num = int(input("Enter the Number: "))
# result = dosum(num)
# print(f"Sum of digits: {result}")

def dosum(num):
    return sum(int(d) for d in str(abs(num)))

num = int(input("Enter the Number: "))
print(f"Sum of digits: {dosum(num)}")