4. Write a program to find whether a given username contains less than 10 characters or not.


name=str(input("Enter Username: "))
l=len(name)
#print(l)
if l<10:
    print("username contains less than 10 characters")
else:
    print("username contains greater than than 10 characters")