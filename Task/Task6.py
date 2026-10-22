# # Vocabulary Comparison of Two Books
# 6.	Write a program to analyze the vocabulary used in two different books. You need to:
# ●	Find all unique words used in each book.
# ●	Identify the common words between both books.
# ●	Identify words that are unique to each book (not found in the other book).
# ●	Display the total number of unique words across both books.
# Tasks:
# ●	Use sets to find the unique words in each text, and perform set operations to find the union, intersection, and differences.

# book1 = input("Enter text of Book 1: ")
# book2 = input("Enter text of Book 2: ")

# words1 = set(book1.lower().split())
# words2 = set(book2.lower().split())

# print("\nUnique words in Book 1:")
# print(words1)

# print("\nUnique words in Book 2:")
# print(words2)

# print("\nCommon words:")
# print(words1 & words2)

# print("\nWords only in Book 1:")
# print(words1 - words2)

# print("\nWords only in Book 2:")
# print(words2 - words1)
# all_words = words1 | words2

# print("\nTotal unique words in both books:", len(all_words))