"""Task4: Three small analysis utilities

1) Project membership analysis using sets
2) Text analysis tool (word counts, frequencies, top-3, vowel count)
3) Book vocabulary comparison (unique words, common words, totals)

Each utility is implemented as a function with a short demo below.
"""

def project_members(project_a, project_b):
    a = set(project_a)
    b = set(project_b)

    print("Members in both projects:", a & b)
    print("Members only in Project A:", a - b)
    print("Members only in Project B:", b - a)
    print("All members:", a | b)


project_a = ["Sahil", "raj ", "Shreya"]
project_b = ["Arvind", "Diya", "Atharv"]

project_members(project_a, project_b)


def text_analysis(text):
    words = text.lower().split()

    print("\nTotal words:", len(words))
    frequency = {}

    for word in words:
        word = word.strip(".,!?")
        frequency[word] = frequency.get(word, 0) + 1

    print("Word frequencies:", frequency)

    top_three = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Top 3 words:", top_three)

    vowels = "aeiou"
    vowel_count = 0

    for char in text.lower():
        if char in vowels:
            vowel_count += 1

    print("Vowel count:", vowel_count)


text = "Python is easy and Python is powerful."
text_analysis(text)

def compare_books(book1, book2):
    words1 = set(book1.lower().split())
    words2 = set(book2.lower().split())

    print("\nUnique words in Book 1:", words1 - words2)
    print("Unique words in Book 2:", words2 - words1)
    print("Common words:", words1 & words2)
    print("Total unique words in Book 1:", len(words1))
    print("Total unique words in Book 2:", len(words2))


book1 = "python is easy to learn"
book2 = "python is easy and powerful"

compare_books(book1, book2)