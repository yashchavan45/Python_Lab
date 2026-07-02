#Create a simple ATM menu system.
pin=1234
print("Welcome to the ATM.\n")
n=int(input("Enter Pin: "))
avl_bal=10000
if n==pin:
    print("Hii there\nwhich trasaction you want to do")
    print("1 for Balance Inquiry\n2 for Withdraw\n3 for Deposit")
    inn=int(input("Enter Here: "))
    if inn==1:
        print("Your available Balance is: ",avl_bal)
    elif inn==2:
        w=int(input("Enter Withdraw Amount: "))
        if w<=avl_bal:
            avl_bal=avl_bal-w
            print("Transaction Sucessful!")
            print("Your available Balance is: ",avl_bal)
        else:
            print("You enter invalid amount or greater than available balance")
    elif inn==3:
        w=int(input("Enter Deposit Amount: "))
        avl_bal=avl_bal+w
        print("Transaction Sucessful!")
        print("Your available Balance is: ",avl_bal)
else:
    print("Incorrect pin.")