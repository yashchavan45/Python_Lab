import math
while True:
    print("===== Math Utility =====")
    print("1.Square Root")
    print("2.Power")
    print("3.Area of Circle")
    print("4.Factorial")
    print("5.Exit")
    try:
        o=int(input("Choose any option."))
    except ValueError:
        print("Enter correct option.")
    if o==1:
        try:
            n=int(input("Enter Number to root: "))
            print(math.sqrt(n))
        except ValueError:
            print("Enter Number Only.")
    elif o==2:
        try:
            n=int(input("Enter Number: "))
            n1=int(input("Enter raised to: "))
            print(pow(n,n1))
        except ValueError:
            print("Enter Number Only.")
    elif o==3:
        try:
            n=int(input("Enter Radius: "))
            area = math.pi * (n ** 2)
            print("Area of circle:", area)
        except ValueError:
            print("Enter Number Only.")
    elif o==4:
         try:
            n=int(input("Enter Number: "))
            print(math.factorial(n))
         except ValueError:
            print("Enter Number Only.")
    elif o==5:
        break