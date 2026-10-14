text = input("Enter the text: ")

stopwords = {"is", "and", "the", "a", "an", "in", "of", "to", "for", "on"}

words = text.split()
cleaned_words = [word for word in words if word.lower().strip(".,!?") not in stopwords]

cleaned_text = " ".join(cleaned_words)

print("Cleaned text:")
print(cleaned_text)