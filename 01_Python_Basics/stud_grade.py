6. Write a program to calculate the grade of a student from his marks from the following
scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 => C
50 – 60 => D
<50 => F


'''90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 => C
50 – 60 => D
<50 => F
'''
s1=int(input("Enter marks of 1st sub: "))
s2=int(input("Enter marks of 2nd sub: "))
s3=int(input("Enter marks of 3rd sub: "))
p=float((s1+s2+s3)/3)
if (p>90):
    print("You passes with Exellent Grade")
elif (p>80 and p<90):
    print("You passed with A Grade.")
elif (p>70 and p<80):
    print("You passed with B Grade.")
elif (p>60 and p<70):
    print("You passed with c Grade.")
elif (p>50 and p<60):
    print("You passed with D Grade.")
else:
    print("You are Failed!")
