# Employee sets for two projects
project1 = {"Amit", "Rahul", "Priya", "Sneha", "Vikas"}
project2 = {"Rahul", "Priya", "Neha", "Vikas", "Rohan"}

# Intersection - employees working on both projects
both_projects = project1.intersection(project2)

# Difference - employees working only on Project 1
only_project1 = project1.difference(project2)

# Difference - employees working only on Project 2
only_project2 = project2.difference(project1)

# Union - all unique employees
all_employees = project1.union(project2)

# Display results
print("Employees in Project 1:", project1)
print("Employees in Project 2:", project2)

print("\nEmployees working on both projects:", both_projects)
print("Employees only in Project 1:", only_project1)
print("Employees only in Project 2:", only_project2)
print("Total unique employees:", all_employees)
print("Number of unique employees:", len(all_employees))