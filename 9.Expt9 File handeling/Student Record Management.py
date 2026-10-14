def display_records():
    with open("students.txt", "r") as file:
        for line in file:
            print(line.strip())

def highest_marks():
    with open("students.txt", "r") as file:
        next(file)
        records = [line.strip().split(",") for line in file]
    student = max(records, key=lambda x: int(x[2]))
    print("Highest Marks:", student[1], student[2])

def average_marks():
    with open("students.txt", "r") as file:
        next(file)
        marks = [int(line.strip().split(",")[2]) for line in file]
    print("Average Marks:", sum(marks) / len(marks))

def above_80():
    with open("students.txt", "r") as file:
        next(file)
        print("Students scoring more than 80:")
        for line in file:
            record = line.strip().split(",")
            if int(record[2]) > 80:
                print(record[0], record[1], record[2])

print("All Records:")
display_records()

highest_marks()
average_marks()
above_80()