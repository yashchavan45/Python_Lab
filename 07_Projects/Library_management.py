books=['It','Holes','Dune','Babel','Room']
borrowed=[]
options=[1,2,3,4,5,6,7]
while True:
    print("==== LIBRARY MENU ====\n")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Borrowed Books")
    print("7. Exit\n")
    while True:
        try:
            choose = int(input("Enter your choice: "))
            if choose in options:
                break
            else:
                print("Please choose from the available options:", options,"\n")
        except ValueError:
            print("Enter numbers only and from the options only\n")
    if choose==1:
        new=input("Enter book name: ")
        books.append(new)
        print("Book added sucessfully.\n")
        print("Avaialbe Books are: ",books,"\n")
    elif choose==2:
        print("Avaialbe Books are: ",books,"\n")
    elif choose==3:
        b=input("Enter Book name: ")
        if b in books:
            borrowed.append(b)
            books.remove(b)
            print("Borrowed Sucessfully.\n")
        else:
            print(b,"not present in the library\n")
    elif choose==4:
        b=input("Enter Book name: ")
        if b in borrowed:
            books.append(b)
            borrowed.remove(b)
            print("Return Sucessfully.\n")
        else:
            print(b,"this book is not borrowed from here.\n")
    elif choose==5:
            b=input("Enter Book name: ")
            if b in books:
                print("Book is present in the library.\n")
            elif b in borrowed:
                print("Book is borrowed.\n")
            else:
                print("This book is not present in library.\n")
    elif choose==6:
        print("Borrowed books are:")
        if not borrowed:
            print("Nothing is borrowed.\n")
        else:
            print("Borrowed books are:")
            print(borrowed)
    elif choose==7:
        print("Thanks visit again...")
        break