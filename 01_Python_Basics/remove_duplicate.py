#Remove duplicate elements from a list.
numbers = list(map(int, input("Enter numbers: ").split()))
unique_numbers = list(set(numbers))
print("List without duplicates:", unique_numbers)