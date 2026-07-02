#Find the second largest number in a list.
numbers = list(map(int, input("Enter numbers: ").split()))
numbers.sort(reverse=True)
print("Second largest:", numbers[1])