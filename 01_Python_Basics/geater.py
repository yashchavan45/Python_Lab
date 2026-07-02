#Find the largest of 5 numbers entered by the user.

n = list(map(int, input("Enter Numbers: ").split()))
n.sort(reverse=True)
#print(n)
for i in n:
    print(i,"is greater")
    break