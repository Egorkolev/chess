x=int(input("Введите Х:"))
a=int(input("Введите число:"))
y=int(input("Введите Y:"))
b=int(input("Введите число:"))
if (x+a+y+b) % 2 != 0:
    print("YES")
elif (x+a) % 2 == 0 and (y+b) % 2 != 0 and (b == 5) or (b == 4):
    print("NO")
else:
    print("NO")

