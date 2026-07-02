#Check whether a number is a perfect number.
n=int(input("Enter No: "))
summ=1
for i in range(2,n):
    if n%i==0:
        summ=summ+i
if n==summ:
    print(n,"This is a Perfect No.")
else:
    print(n,"Not a Perfect NO.")