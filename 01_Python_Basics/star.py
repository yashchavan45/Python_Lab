'''7. Write a program to print the following star pattern.
*
***
***** for n = 3'''
for i in range(1,6):
    for j in range(1,6):
       if j<=i:
           print("*",end="")
       else:
            print(" ",end="")
    print()