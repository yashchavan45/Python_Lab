class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
class Manager(Employee):
    def __init__(self, name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:",self.department)
s = Manager("yash",250000,"computer")
s.display()
