Reverse a string without using slicing.

def reverse_string(s):
    result = ""
    i = len(s) - 1
    while i >= 0:
        result += s[i]
        i -= 1
    return result
print(reverse_string("world"))