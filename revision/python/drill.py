# Exercise section 
# Level 1

# 1. create three variabel...
# number = 67
# name = "Mayank"
# paisa = 67.67
# can_see = True


# 2. convert string 25 into a integer
# string = "25"
# number_string = int(string)
# print(type(number_string))


# 3. 
# num_2 = int(input("Enter second number: "))
# num_1 = int(input("Enter first number: "))
# print(num_1 + num_2)

# 4. 
# remainder = 17 % 3
# print(remainder)

# user_age = int(input("Enter the age: "))
# if user_age >= 18: 
#     print("You are eligible for driving!")
# else: 
#     print("You are not eligible for driving!")

# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))

# if num1 > num2: 
#     print(f"{num1} is greater..")
# else:
#     print(f"{num2} is greater..")


# num = int(input("Enter the number: "))
# if num % 2 == 0:
#     print("The number is even..")
# else:
#     print("The number is odd..")

# num = int(input("Enter a number: "))
# print(f"The square of the {num} is {num**2}")
# print(f"The cube of the {num} is {num**3}")

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"My name is {name} and I am {age} years old...")

# f = (c*9/5) + 32

# celci_temp = int(input("Enter the temperatre in degree celcious: "))
# print(f"The temperature in farenheit is {(celci_temp*9/5) + 32}")

# num = int(input(":Enter the number: "))
# if num == 0:
#     print("The number is zero..")
# elif num >0:
#     print("The number is positive..")
# else:
#     print("The number is negative...")

# str_num = input("Enter a number: ")
# print(int(str_num) + 10)

# num1 = int(input("Enter the first numnber: "))
# num2 = int(input("Enter the second numnber: "))
# num3 = int(input("Enter the third numnber: "))

# print(f"The avarage of {num1},{num2} and {num3} is {(num1+num2+num3) / 3}")

# num = int(input("Enter the number: "))
# if num> 10 and num < 50:
#     print("The number lies between 10 and 50..")
# else:
#     print("The number does not lie between 10 and 50..")

# Simple calculator...

# num1 = int(input("Enter the fist number: "))
# ope = input("Enter the operator..: ")
# num2 = int(input("Enter the second number: "))

# if ope == "+":
#     print(f"{num1+num2}")
    
# elif ope == "-":
#     print(f"{num1-num2}")
# elif ope == "*":
#     print(f"{num1*num2}")
# elif ope == "/":
#     print(f"{num1/num2}")

"""
2. User Info Processor

Program should:

Take name, age, height

Convert types properly

Print formatted summary

Check if user is adult

Calculate birth year (approx)
"""

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# height = int(input("Enter your height(in cm..): "))

# if age >= 18:
#     life_stage = "Yes.."

# elif age<0 or age ==0:
#     print("Enter valid age..")
#     life_stage = "Null.."

# else:
#     life_stage = "No.."

# birth_year = 2026 - age

# summary = f"""
# Name: {name}
# Age: {age}
# Height: {height} cm
# Adult: {life_stage}
# Approximate Birth Year: {birth_year} approx..
# """

# print(summary)

# num = int(input("Enter the number: "))
# if num > 0:
#     print("The number is positive...")
# elif num < 0:
#     print("The number is negative...")
# else:
#     print("The number is zero...")


# for i in range(1,11):
#     print(i)

# a = 0
# while True:
#     a += 1
#     print(a)
#     if a == 10:
#         break

# for i in range(1,21):
#     if i%2 == 0:
#         print(f'Even numbers: {i}')
#     if i%2 != 0:
#         print(f'Odd numbers: {i}')

# for i in range(1,31):
#     if i%3 == 0:
#         print(i)
 
# for i in range(1,7):
#     if i == 5:
#         continue
#     print(i)

# for i in range(1,6):
#     for i in range(1,11):
#         print(f"{2*i}")

# inp = input("Enter any text: ")
# if inp == "":
#     print("The string is empty...")
# else:
#     print("The string is not empty...")

# sr = "Iamthebest"
# for i in sr:
#     print(i)

# num = int(input("Enter the number: "))

# if (num == 0 or num > 0) and num < 50:                       doubt........
#     print("The number is in the range of 0 to 50..") 
#     if (num == 50 or num > 50) and num < 100:
#         print("The number is in the range of 50 to 100..") 


# ---------------password checker doubt..........

# text = input("Enter the thing......: ")
# if text == text[::-1]:
#     print("The text is palindrom..")
# else:
#     print("The text is not plandrom...")

# num = int(input("Enter the number: "))
# a = 0
# b = 0
# while True:
#     if a == num:
#         print(f"The sum of numbers from 1 to {num} is {b}")
#         break
#     a += 1
#     # print("Index: ",a)
#     b = b + a
#     # print("The sum value: ",b)


# text = input("Enter the text: ")
# total = [] 
# sum = 0
# for i in "aeiou":
#     total.append(text.count(i))
# for i in total:
#     sum = sum + i
# print(f"The total number of vowel: {sum}")


# list = [5,7,2,8,1,69]
# # print(list.index(2))
# condition = []
# for i in range(0,len(list)):
#     for d in list:
#         if list[i] >= d:
#             condition.append("T")             # Nice qusetion...
#         else:
#             condition.append("F")
#     # print(condition)
#     if not("F" in condition):
#         print(f"{list[i]} is the largest number....")
#     condition = []


# string = input("Enter any text: ")
# l = []
# for i in string:
#     l.append(i)
# l.reverse()
# st = ""
# for i in l:
#     st = st + i    
# print(st)

# for i in range(1,5):
#     print(i*"*")

# Number guessing game.......
# import random
# # print(cu_num)
# while True:
#     cu_num = random.randint(1,100)
#     user_num = input("Enter the guess number (press 'q' to quit): ")
#     if user_num == "q":
#         print("Exititng game.........")
#         break
#     if cu_num == int(user_num) :
#         print(f"The guess was correct and the number is {cu_num}")
#     else:
#         print(f"The guess number is incorrect and the number is {cu_num}")
        
# Factorial using while.....
# n = int(input("Enter the number for factorial...: "))
# l = 1
# while True:
#     if n == 0 :
#         break
#     l = l * n
#     n = n - 1
#     # print(n)
# print(l)    

# def factorial():
#     n = int(input("Enter the number for factorial...: "))
#     l = 1
#     while True:
#         if n == 0 :
#             n = l
#             l = 1
#             # break
#         l = l * n
#         print(l)
#         n = n - 1
#     # n = l
#     # print(n)
#     print(l) 
       

# factorial()

# to check the wheither the number is prime or not ....

# number = int(input("Enter the number: "))
# if number == 2:
#     print("The number is prime...")
# elif number == 1:
#     print("1 is neither prime nor composite..")

# else:
#     for i in range(2,number):
#         if number % i == 0:
#             print("This number is not prime...")
#             break
#     else:
#         print("This number is prime..")
        

# fibbonachi series...
