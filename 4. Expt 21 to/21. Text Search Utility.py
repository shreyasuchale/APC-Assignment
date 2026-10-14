text = input("Enter the text: ")
query = input("Enter search query: ")

count = text.lower().count(query.lower())
highlighted = text.lower().replace(query.lower(), "**" + query.lower() + "**")

print("Number of occurrences:", count)
print("Highlighted text:")
print(highlighted)