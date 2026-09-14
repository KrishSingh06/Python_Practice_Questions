#7  write a program in python to define a method checkarmstrong(num) that will return if num is an armstrong no or else return false 
 
def checkArmstrong(num):
    temp=num
    temp1=num
    c=0
    while(num>0):
        c=c+1
        num = num//10
    sum=0
    
    while temp>0:
        d = temp % 10
        sum = sum + d**c
        temp =temp//10
    
    return sum == temp1
num = int(input("enter a number: "))
print(checkArmstrong(num))

