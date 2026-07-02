try:
    n=int(input("Enter Number: "))
    nn=int(input("Enter Number: "))    
except ValueError:
    print("Enter Numbers Only.")
try:
    summ=n/nn
    print(summ)
except ZeroDivisionError:
    print("Can't Divide Any Number by Zero")