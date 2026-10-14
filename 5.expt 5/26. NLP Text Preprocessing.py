import re

text = input("Enter the text: ")

contractions = {
    "don't": "do not",
    "can't": "cannot",
    "won't": "will not",
    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",
    "didn't": "did not",
    "doesn't": "does not",
    "couldn't": "could not",
    "wouldn't": "would not",
    "shouldn't": "should not",
    "i'm": "i am",
    "you're": "you are",
    "he's": "he is",
    "she's": "she is",
    "it's": "it is",
    "we're": "we are",
    "they're": "they are",
    "i've": "i have",
    "you've": "you have",
    "we've": "we have",
    "they've": "they have"
}

text = text.lower()

for contraction, expansion in contractions.items():
    text = text.replace(contraction, expansion)

text = re.sub(r'[^a-zA-Z\s]', '', text)
text = re.sub(r'\s+', ' ', text).strip()

print("Cleaned text:", text)