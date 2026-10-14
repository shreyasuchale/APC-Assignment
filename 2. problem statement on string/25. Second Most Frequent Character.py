s = input("Enter a string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(items) >= 2:
    print("Second Most Frequent Character:", items[1][0])
    print("Frequency:", items[1][1])
else:
    print("No second most frequent character")