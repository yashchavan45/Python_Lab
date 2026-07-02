#Build a rock-paper-scissors game.
import random
print("...Welcome To ROCK-PAPER-SCISSORS Game!...")
print("<<<GAME RULES>>>")
print(" You have 3 chances if you beat me get 1 point")
print(" Score Maximum Points.  GOOD LUCK!\n")
l1=["ROCK","PAPER","SCISSOR"]
print(l1)
print("1. for 'ROCK'\n2. for 'PAPER\n3. for 'SCISSORS")
score=0
for i in range(1,4):
    temp = random.choice(l1)
    n = int(input("Enter Your Number: "))
    if (n == 1 and temp == "SCISSOR") or \
       (n == 2 and temp == "ROCK") or \
       (n == 3 and temp == "PAPER"):
        print("Wow! you beat me and earn 1 point.\nmine was", temp, "\n")
        score += 1
    elif (n == 1 and temp == "ROCK") or \
         (n == 2 and temp == "PAPER") or \
         (n == 3 and temp == "SCISSOR"):
        print("It's a tie!\nmine was", temp, "\n")
    else:
        print("Oops! you lost.\nmine was", temp, "\n")

print("You score",score)