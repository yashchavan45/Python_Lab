Count vowels and consonants in a string.

s = str(input("Enter string: "))
v = ('a', 'e', 'i', 'o', 'u')
vowels = 0
for char in s:
    if char.lower() in v:   
        vowels += 1
print("Number of vowels:", vowels)