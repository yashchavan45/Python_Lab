import random
print("===== Guess The Number =====")
print("Guess a number (1-100): ")
r=random.randint(1,100)
n=0
i=1
while(n!=r):
    try:
        n=int(input("Enter your guess: "))
        i+=1
    except ValueError:
        print("Enter Number Only.")
    if n==r:
        print("Congrats! you guessed correct.")
        print("you guessed the number in",i,"attempts.")
    elif n>r:
        print("your guess is high.")
        print("Try again.")
    elif n<r:
        print("your guess is low.")
        print("Try again.")