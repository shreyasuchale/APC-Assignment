# 5.	Write a program to build a simple text analysis tool. The tool should perform the following operations on a given paragraph of text:
# ●	Count the total number of words.
# ●	Count the frequency of each word.
# ●	Identify and display the top 3 most frequent words.
# ●	Count the number of vowels in the entire text.
# Tasks:
# ●	Use string manipulation to split the text into words and to check for vowels.
# ●	Use a dictionary to store the word frequencies.

text = input("Enter a paragraph: ")
words = text.lower().split()

print("Total number of words:", len(words))
frequency = {}

for word in words:
    word = word.strip(".,!?")
    
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:")
print(frequency)

top_3 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 most frequent words:")
for word, count in top_3:
    print(word, ":", count)

vowels = "aeiou"
vowel_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1

print("Total number of vowels:", vowel_count)