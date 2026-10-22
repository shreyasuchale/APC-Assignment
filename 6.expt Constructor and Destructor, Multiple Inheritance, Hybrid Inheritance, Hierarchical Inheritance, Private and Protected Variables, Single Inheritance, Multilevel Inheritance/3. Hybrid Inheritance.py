class Person:
    def person_info(self):
        print("Person: Rahul")

class Student(Person):
    def student_info(self):
        print("Student")

class Employee(Person):
    def employee_info(self):
        print("Employee")

class Manager(Student, Employee):
    def manager_info(self):
        print("Manager")

manager = Manager()
manager.person_info()
manager.student_info()
manager.employee_info()
manager.manager_info()