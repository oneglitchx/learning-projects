# # This file is just for dumping the codes for the immediate test and 
# # trying out new things 

# class Employee:
#     def __init__(self,name, age, salary):
#         self.name = name 
#         self.age = age
#         self.salary = salary
    
#     company = "BOSTON DYNAMICS"

#     def info(self):
#         print(f"The name : {self.name}\nThe age: {self.age}\nThe salary: {self.salary}")


#     def increment_salary(self,value):
#         self.salary += value

#     def __difference__(self, obj):
#         if self.salary > obj.salary:
#             print(f"The salary difference is: {self.salary - obj.salary}")
#         else:
#             print(f"The salary difference is: {obj.salary - self.salary}")
    
#     def __str__(self):
#         print("The is the __str__ method")

#     def __add__(self, obj):
#         return f"{self.salary + obj.salary}"

#     def __len__(self):
#         print("No any length")

# a = Employee("Mayank Kashyap", 17, 500000)
# b = Employee("Sam Altman",41, 2000000)

# a.__add__(b)
# # print(a + b)

# import json

# jjson = {"name": "Mayank Kashyap","age": 17}
# with open("data.json","r") as f:
#     contants = f.read()
#     print(contants)
#     gg = json.load("data.json")
#     print(type(gg))

# import os

# l = os.listdir()
# print(l)

# d = {"hello": "HOlskdjflkj", "yo": "mou"}
# print(d.keys())
# print(type(d.keys()))
# a = []
# for i in d.keys():
#     a.append(i)
#     print(i)
# print(a)

# import json
# with open('data.json',"r") as f:
#     conDict = json.load(f)
#     dates = []
#     for i in conDict.values():
#         dates.append(i)
#         print(dates)
#     print("this is the lsit")
#     print(dates)
# print(type(conDict))
# if n:= len([34,34,34,34,34,34]) > 3:
    # print(n)


# def table(a: int) -> str:
#     for i in range(1,11):
#         print(f"{a} X {i} = {a*i}")

# table(3)

# from typing import List, Tuple, Dict

# l : List[int] = [34,34,54,67,3]

# ask = int(input("Enter the number: "))
# match ask:
#     case 34:
#         print("Hey")
#     case 45:
#         print("YOU Hell !")
#     case _:
#         print("Nothing to to match here!")

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# merged = dict1 | dict2
# print(merged)
# l = merged.keys()
# print(l)

# with (
#     open("data.json") as f1,
#     # open("") as f2
# ):

#     contant = f1.read()
#     print(contant)

# try:
#     a = int(input("Enter a valid number: "))
# except Exception as e:
#     print(e)
# else:
#     print("The program was run successfully.")


d = {
    1: {
        "This is the questions?" : ["hi","hello","The end will be the answer"]
    },
    2: {
        "This is the questions?" : ["These are the options","The end will be the answer"]
    },
    3: {
        "This is the questions?" : ["These are the options","The end will be the answer"]
    }
}


# print(d.keys())
# print(d.get(1))
# print(d.get(1).get("This is the questions?"))
# print(d.get(1).keys())
# question = list(d.get(1).keys())
# a, = question
# print(a)
# print(question)

# options = d.get(1).get(a)
# print(options)

# option_serial = {
#     1: "a.",
#     2: "b.",
#     3: "c.",
#     4: "d."
# }
# for index,i in enumerate(options):
#     if options[-1] == i:
#         break 
#     print(option_serial.get(index),i)
d.pop(1)
# for i in d:
#     print(d.pop())
print(list(d.keys()))