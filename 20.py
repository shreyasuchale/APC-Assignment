import string

filename = input("Enter the text file name: ")

with open(filename, "r") as file:
    text = file.read()

text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))

words = text.split()

word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("Total number of words:", len(words))

print("\n10 Most Frequent Words:")
sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

for word, frequency in sorted_words[:10]:
    print(word, ":", frequency)