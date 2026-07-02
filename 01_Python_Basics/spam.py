3. A spam comment is defined as a text containing following keywords: “Make a lot of
money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.


strr=str(input("Enter your input: "))
#print(strr)Make a lot of
lis=( "money", "buy now", "subscribe this", "click this")
for i in range(4) :
    if (lis[i])==strr:
        print("STOP IT`S A SPAM")
        break
else:
        print("Not spam.")
