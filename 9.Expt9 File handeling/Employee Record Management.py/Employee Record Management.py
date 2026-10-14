def display_employees():
    with open("employees.txt", "r") as file:
        for line in file:
            print(line.strip())

def highest_paid():
    with open("employees.txt", "r") as file:
        next(file)
        employees = [line.strip().split(",") for line in file]
    employee = max(employees, key=lambda x: int(x[3]))
    print("Highest-Paid Employee:", employee[1], employee[3])

def average_salary():
    with open("employees.txt", "r") as file:
        next(file)
        salaries = [int(line.strip().split(",")[3]) for line in file]
    print("Average Salary:", sum(salaries) / len(salaries))

def above_salary():
    salary = int(input("Enter salary: "))
    with open("employees.txt", "r") as file:
        next(file)
        print("Employees earning above", salary, ":")
        for line in file:
            employee = line.strip().split(",")
            if int(employee[3]) > salary:
                print(employee[0], employee[1], employee[3])

print("All Employees:")
display_employees()

highest_paid()
average_salary()
above_salary()