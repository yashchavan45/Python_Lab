import random
import time
print("===== Beat The Dice =====")
r=random.randint(1,6)
ys=0
cs=0
i="y"
while(i!="n"):
    try:
        print("Rolling Dice...")
        time.sleep(2)
        n=int(input("Enter your guess: "))
        print("your roll:",n)
        print("computer roll:",r)
    except ValueError:
        print("Enter Number Only.")
    if n>r:
        print("You win!\n")
        ys+=1
        print("your score:",ys)
        print("computer score:",cs)
        i=input("Play Again? (y/n)")
    elif n<r:
        print("You Lost.")
        cs+=1
        print("your score:",ys)
        print("computer score:",cs)
        i=input("Play Again? (y/n)\n")
    else:
        print("It's a Tie.")
        print("your score:",ys)
        print("computer score:",cs)
        i=input("Play Again? (y/n)")
        
        
        