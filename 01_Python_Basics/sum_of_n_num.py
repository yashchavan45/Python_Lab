#5. Write a program to find the sum of first n natural numbers using while loop.

n=int(input("Enter Number: "))
s=0
for i in range(n+1):
    s=s+i
print(s)