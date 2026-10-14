import re

text = input("Enter the text: ")

abbreviations = ["Mr.", "Mrs.", "Dr.", "Ms.", "Prof."]
placeholder = {}

for i, abbr in enumerate(abbreviations):
    key = f"ABBR{i}"
    placeholder[key] = abbr
    text = text.replace(abbr, key)

sentences = re.split(r'(?<=[.!?])\s+', text)

for i, sentence in enumerate(sentences):
    for key, abbr in placeholder.items():
        sentence = sentence.replace(key, abbr)
    sentences[i] = sentence.strip()

print("\nSentences:")
for i, sentence in enumerate(sentences, 1):
    print(i, ".", sentence)