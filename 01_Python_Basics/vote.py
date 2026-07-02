#Create a voting system for 5 candidates.
bjp=0
aam=0
sena=0
congress=0
shinde=0
print("1 for BJP\n2 for aam\n3 for sena\n4 for congress\n5 for shinde")
n=int(input("Enter How many voters are there."))
for i in range(1,n+1):
    v=int(input("Enter your vote: "))
    if v==1:
        bjp+=1
    elif v==2:
        aam+=1
    elif v==3:
        sena+=1
    elif v==4:
        congress+=1
    elif v==5:
        shinde+=1
    else:
        print("invalid vote\ntry again")
        i=i-1
if bjp>aam and bjp>sena and bjp>congress and bjp>shinde:
    print("Bjp won the Election!")
elif bjp<aam and aam>sena and aam>congress and aam>shinde:
    print("Aam won the Election!")
elif sena>aam and bjp<sena and sena>congress and sena>shinde:
    print("sena won the Election!")
elif congress>aam and congress>sena and congress>bjp and congress>shinde:
    print("congress won the Election!")
elif shinde>aam and shinde>sena and shinde>congress and bjp<shinde:
    print("shinde won the Election!")