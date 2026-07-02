class Person:
    def __init__(self, name):
        self.name = name

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s = Child("yash", 20)
s.display()
