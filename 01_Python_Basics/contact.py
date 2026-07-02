contacts = {
    "yash": 8799865241,
    "soham": 8080833478
}

print("You want to search or add a contact.")
print("1 for search\n2 for add new contact")
n = int(input("enter here: "))

if n == 1:
    s = input("Search Name here: ")
    if s in contacts:
        print(s, contacts[s])
    else:
        print("Contact not found.")
elif n == 2:
    name = input("Enter new contact name: ")
    number = int(input("Enter contact number: "))
    contacts[name] = number
    print("Contact added successfully.")
    print(contacts)
else:
    print("Invalid choice.")
