#Create a password strength checker.
s=str(input("Enter your password: "))
l=len(s)
if l<8:
    print("Your password is week min 8 char is required.")
elif l>8 and "@" in l:
    print("your password is strong enough.")