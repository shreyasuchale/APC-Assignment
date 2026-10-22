# 1. Write a program to building a simple student grade management system for a class of students.
# The system will store student names and their grades (both as lists) 
# should be able to perform the following operations:

# Add a new student and their grade.
# Update the grade of an existing student.
# Remove a student from the list.
# Calculate and display the average grade of the class.
# Display the highest and lowest grades in the class.


students = []
grades = []

def add_student():
    name = input("Enter Student Name: ")
    grade = float(input("Enter Student Grade: "))

    students.append(name)
    grades.append(grade)

    print("Student Added Successfully.")

def update_student():
    name = input("Enter Student Name to Update: ")

    if name in students:
        index = students.index(name)
        grades[index] = float(input("Enter New Grade: "))
        print("Grade Updated Successfully.")
    else:
        print("Student Not Found.")


def remove_student():
    name = input("Enter Student Name to Remove: ")
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student Removed Successfully.")
    else:
        print("Student Not Found.")

def average_grade():
    if len(grades) > 0:
        average = sum(grades) / len(grades)
        print("Average Grade =", average)
    else:
        print("No Student Records.")

def highest_lowest():
    if len(grades) > 0:
        print("Highest Grade =", max(grades))
        print("Lowest Grade =", min(grades))
    else:
        print("No Student Records.")

def display_students():
    if len(students) > 0:
        print("\nStudent Name\tGrade")
        for i in range(len(students)):
            print(students[i], "\t\t", grades[i])
    else:
        print("No Student Records.")

while True:
    print("\n===== Student Grade Management System =====")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Display Highest and Lowest Grade")
    print("6. Display All Students")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))
    match choice:
        case 1:
            add_student()
        case 2:
            update_student()
        case 3:
            remove_student()
        case 4:
            average_grade()
        case 5:
            highest_lowest()
        case 6:
            display_students()
        case 7:
            print("Program Ended.")
            break
        case _:
            print("Invalid Choice!")