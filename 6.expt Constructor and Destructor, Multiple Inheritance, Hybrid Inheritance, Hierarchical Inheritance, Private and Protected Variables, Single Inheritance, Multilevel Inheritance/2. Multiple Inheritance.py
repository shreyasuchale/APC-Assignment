class Father:
    def father_info(self):
        print("Father: Rajesh")

class Mother:
    def mother_info(self):
        print("Mother: Sunita")

class Child(Father, Mother):
    def child_info(self):
        print("Child: Rahul")

child = Child()
child.father_info()
child.mother_info()
child.child_info()