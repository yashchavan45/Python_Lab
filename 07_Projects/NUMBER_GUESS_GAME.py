#Build a number guessing game.
import random
print("...Welcome To Number Guessing Game!...")
print("<<<GAME RULES>>>")
print(" You have 5 chances any correct match get 1 point")
print(" Score Maximum Points.  GOOD LUCK!\n")
l1=[1,2,3,4,5,6,7,8,9,0]
print(l1)
print("guess any numbers between above list.\n")
score=0
for i in range(1,6):
    temp=random.choice(l1)
    n=int(input("Enter Your Number: "))
    if n==temp:
        print("Wow! you guess correct and earn 1 point.\n")
        score=score+1
    else:
        print("wrong guess correct one is",temp,"\n")
print("You score",score)