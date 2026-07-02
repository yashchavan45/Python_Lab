1. Write a program to find the greatest of four numbers entered by the user.

a=int(input("Enter Number a: "))
b=int(input("Enter Number b: "))
c=int(input("Enter Number c: "))
d=int(input("Enter Number d: "))
if a>b and a>c and a>d:
    print("a is greter")
elif a<b and b>c and b>d:
    print("b is greter")
elif c>b and c>a and c>d:
    print("a is greter")
else:
    print("d is greater")