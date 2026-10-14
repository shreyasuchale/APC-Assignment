

student_names = []
student_grades = []



def add_student(name, grade):
    student_names.append(name)
    student_grades.append(grade)
    print(name, "has been added with grade", grade)



def update_grade(name, new_grade):
    if name in student_names:
        index = student_names.index(name)
        student_grades[index] = new_grade
        print(name, "'s grade has been updated to", new_grade)
    else:
        print("Student not found.")



def remove_student(name):
    if name in student_names:
        index = student_names.index(name)
        student_names.pop(index)
        student_grades.pop(index)
        print(name, "has been removed.")
    else:
        print("Student not found.")



def calculate_average():
    if len(student_grades) == 0:
        print("No grades available.")
    else:
        average = sum(student_grades) / len(student_grades)
        print("Average grade:", round(average, 2))


# Function to display highest and lowest grades
def display_extreme_grades():
    if len(student_grades) == 0:
        print("No grades available.")
    else:
        print("Highest grade:", max(student_grades))
        print("Lowest grade:", min(student_grades))


# Function to display all students
def display_students():
    if len(student_names) == 0:
        print("No students available.")
    else:
        print("\nStudent Details:")
        for i in range(len(student_names)):
            print(student_names[i], ":", student_grades[i])


# Main program
while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Display Highest and Lowest Grades")
    print("6. Display All Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        add_student(name, grade)

    elif choice == "2":
        name = input("Enter student name: ")
        new_grade = float(input("Enter new grade: "))
        update_grade(name, new_grade)

    elif choice == "3":
        name = input("Enter student name: ")
        remove_student(name)

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        display_extreme_grades()

    elif choice == "6":
        display_students()

    elif choice == "7":
        print("Thank you for using the Student Grade Management System.")
        break

    else:
        print("Invalid choice. Please try again.")