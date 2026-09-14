# wap to take input of two number and check whether no is even and odd

x = float(int(input("Enter the First no :")))
y = float(int(input("Enter the Second no :")))


if x % 2 == 0:
    print(f"{int(x)} is even")
else:
    print(f"{int(x)} is odd")

if y % 2 == 0:
    print(f"{int(y)} is even")
else:
    print(f"{int(y)} is odd")