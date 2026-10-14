s = input("Enter a sentence: ")

count = 0
word = False

for ch in s:
    if ch != " " and word == False:
        count += 1
        word = True
    elif ch == " ":
        word = False

print("Total Words:", count)