4. Write a program to find whether a given number is prime or not.


n=int(input("Enter Number: "))
for i in range(2,n):
    if n%2==0:
        print("Not Prime")
        break
else:
    print("Prime Number.")