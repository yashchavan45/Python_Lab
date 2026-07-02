#Find the sum of digits of a number.
n=int(input("Enter Number: "))
digit=0
summ=1
while(n>0):
    digit=n%10
    summ=summ*digit
    n= n//10
print("Product is: ",summ)