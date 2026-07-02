2. Write a program to find out whether a student has passed or failed if it requires a total of
40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
input from the user.

s1=int(input("Enter marks of 1st sub: "))
s2=int(input("Enter marks of 2nd sub: "))
s3=int(input("Enter marks of 3rd sub: "))
p=float((s1+s2+s3)/3)
if (p>40):
    print("You passes with ",p,"% Congrats!")
elif ((s1/3)>32 and (s2/3)>32 and (s3/3)>32 ):
    print("You just passed.")
else:
    print("You are Failed!")
