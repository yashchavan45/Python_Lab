#Find the GCD of two numbers.
def find_hcf(x, y):
    smaller = min(x, y)
    hcf = 1
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

print(f"The GCD of {n1} and {n2} is {find_hcf(n1, n2)}")