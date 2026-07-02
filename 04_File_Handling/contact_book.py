print("This is the contact book app")
n=input("Enter Number to choose from menu\n")

def main_menu():
    print("\nMain Menu")
    print("1. Add New Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")

def add_contact():
    with open("contact_book.txt", "a") as file:
        name = input("Enter Name: ")
        number = input("Enter Number: ")
        file.write(f"Name : {name}\n")
        file.write(f"Number : {number}\n")
    print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    with open("contact_book.txt", "r") as file:
        contacts = file.readlines()
        for i in range(len(contacts)):
                if name in contacts[i]:
                    print(contacts[i],end=" ")
                    print(contacts[i+1],end=" ")
                    break
        else:
            print("Contact not found.")
def delete_contact():
    name = input("Enter name to delete: ")
    with open("contact_book.txt", "r") as file:
        contacts = file.readlines()
    for i in range(len(contacts)):
        if name in contacts[i]:
            del contacts[i:i+2]
            with open("contact_book.txt", "w") as file:
                file.writelines(contacts)
            print("Contact deleted successfully!")
            break
    else:
        print("Contact not found.")
while True:
    main_menu()
    n = input("\nEnter Choice: ")
    if n == "1":
        add_contact()
    elif n == "2":
        search_contact()
    elif n == "3":
        delete_contact()
    elif n == "4":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Try again.")
        