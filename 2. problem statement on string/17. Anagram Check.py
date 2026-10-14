s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

a = sorted(s1)
b = sorted(s2)

if a == b:
    print("Anagram")
else:
    print("Not Anagram")