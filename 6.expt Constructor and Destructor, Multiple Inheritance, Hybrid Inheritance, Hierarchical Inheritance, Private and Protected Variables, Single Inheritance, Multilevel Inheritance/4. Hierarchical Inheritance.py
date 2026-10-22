class Person:
    def person_info(self):
        print("Name: Shreyas Uchale")
        print("Age: 22")

class Employee(Person):
    def employee_info(self):
        print("Employee ID: E101")
        print("Salary: 80k")

class Student(Person):
    def student_info(self):
        print("Roll No: 143")
        print("Course: CSE")

employee = Employee()
student = Student()

employee.person_info()
employee.employee_info()

student.person_info()
student.student_info()