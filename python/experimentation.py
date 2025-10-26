# This file is just for dumping the codes for the immediate test and 
# trying out new things 

class Employee:
    def __init__(self,name, age, salary):
        self.name = name 
        self.age = age
        self.salary = salary
    
    company = "BOSTON DYNAMICS"

    def info(self):
        print(f"The name : {self.name}\nThe age: {self.age}\nThe salary: {self.salary}")


    def increment_salary(self,value):
        self.salary += value

    def __difference__(self, obj):
        if self.salary > obj.salary:
            print(f"The salary difference is: {self.salary - obj.salary}")
        else:
            print(f"The salary difference is: {obj.salary - self.salary}")
    
    def __str__(self):
        print("The is the __str__ method")

    def __add__(self, obj):
        return f"{self.salary + obj.salary}"

    def __len__(self):
        print("No any length")

a = Employee("Mayank Kashyap", 17, 500000)
b = Employee("Sam Altman",41, 2000000)

a.__add__(b)
# print(a + b)
