filename = input("Enter input file name: ")
target = input("Enter word or phrase to replace: ")
replacement = input("Enter replacement word or phrase: ")
output_file = input("Enter output file name: ")

with open(filename, "r") as file:
    text = file.read()

count = text.lower().count(target.lower())
text = text.replace(target, replacement)

with open(output_file, "w") as file:
    file.write(text)

print("Number of replacements:", count)
print("Modified text saved to", output_file)