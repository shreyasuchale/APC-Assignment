class Person:
    def __init__(self):
        self._name = "Shreyas Uchale"
        self.__age = 22

    def _display_name(self):
        print("Name:", self._name)

    def __display_age(self):
        print("Age:", self.__age)

    def display_person(self):
        self._display_name()
        self.__display_age()

class Employee(Person):
    def __init__(self):
        super().__init__()
        self._employee_id = "A143"
        self.__salary = 80000

    def display_employee(self):
        self.display_person()
        print("Employee ID:", self._employee_id)
        print("Salary:", self.__salary)

class Manager(Employee):
    def __init__(self):
        super().__init__()
        self._department = "CSE"

    def display_manager(self):
        self.display_employee()
        print("Department:", self._department)

manager = Manager()
manager.display_manager()