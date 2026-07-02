#Take 10 numbers from the user and count how many are even and odd.

n = list(map(int,input("Enter Numbers: ").split()))
#print(n)
even=0
odd=0
for i in n:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Ever: ",even)
print("Odd: ",odd)