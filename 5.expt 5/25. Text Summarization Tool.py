import re
from collections import Counter

text = input("Enter the text: ")

sentences = re.split(r'(?<=[.!?])\s+', text.strip())

stopwords = {"the", "is", "a", "an", "and", "of", "to", "in", "for", "on", "with", "are", "this", "that", "it"}

words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
frequency = Counter(word for word in words if word not in stopwords)

scores = {}

for sentence in sentences:
    sentence_words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
    scores[sentence] = sum(frequency[word] for word in sentence_words)

top_sentences = sorted(scores, key=scores.get, reverse=True)[:3]

print("\nSummary:")
for sentence in top_sentences:
    print(sentence)