class Student:
    tutor = "Bindu miss"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name of student is :",self.name)
        print("The age of student is :",self.age)
        print("Tutor name :",Student.tutor)
        print("\n")

    def compare(self,other):
        if self.age == other.age:
            print("Both are same age")
        else:
            print("Both are not same age")

s1 = Student("Basam",21)
s2 = Student("mishal",21)
s1.display()
s2.display()

s1.compare(s2)