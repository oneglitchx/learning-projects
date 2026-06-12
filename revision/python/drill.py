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

# if (num == 0 or num > 0) and num < 50:                       #doubt........
#     print("The number is in the range of 0 to 50..") 
# elif (num == 50 or num > 50) and num < 100:
#     print("The number is in the range of 50 to 100..") 


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
# cu_num = random.randint(1,100)
# print(cu_num)
# while True:
#     user_num = input("Enter the guess number (press 'q' to quit): ")
#     if user_num == "q":
#         print("Exititng game.........")
#         break
#     if cu_num == int(user_num) :
#         print(f"The guess was correct and the number is {cu_num}")
#     else:
#         print(f"The guess number is incorrect and the number is {cu_num}")
#         break
        
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
#             break
#         l = l * n
#         n = n - 1
#         # print(n)
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
        

# # fibbonachi series...
# ask = int(input("Enter the number: "))
# fibbonachi_num_series = []
# preciding_num1 = 0
# preciding_num2 = 1
# for i in range(1,ask+1): 
#     # print("The index",i)

#     if i == 1:
#         fibbonachi_num_series.append(0)
#     summation = preciding_num1 + preciding_num2 
#     fibbonachi_num_series.append(summation)
#     # print("The summation value",summation)
#     preciding_num1 = preciding_num2
#     # print("The precidintnum1",preciding_num1)
#     preciding_num2 = summation
#     # print("precidingnum2", preciding_num2)
#     # print("The list...",fibbonachi_num_series)
# # fibbonachi_num_series.insert(1,1)
# print(fibbonachi_num_series)
    

# fibbonachi series...

# n = int(input("Enter the number: "))
# fibbonachi_num_series = []
# fisrt_preceding = 0
# second_preceding = 1

# for i in range(1,n + 1):
#     if i == 1:
#         fibbonachi_num_series.append(fisrt_preceding)
#     if i == 2:
#         fibbonachi_num_series.append(second_preceding)
    
#     else:
#         summation = fisrt_preceding + second_preceding
#         fibbonachi_num_series.append(summation)

#         fisrt_preceding = second_preceding
#         second_preceding = summation
    
# print(fibbonachi_num_series)






# # count the even number in the list

# list = [1,2,3,4,5,6,8,10,9]
# n = 0
# for index,i in enumerate(list):
#     if list[index] %2 == 0:
#         n = n +1
# print(n) 

# Removing all white spaces using loop
# text = input("Enter the text: ")
# l = []
# for i in text:
#     if i == " ":
#         continue
#     l.append(i)
# print(l)

# st = ""
# for i in l:
#     st = st + i

# print(st)

# printing all number which divides by 7 but not 5 
# till_which_no = int(input("Enter the numcer till which u want to find out the divisibility:"))
# l = []
# for i in range(1,till_which_no+1):
#     if i % 7 == 0 and i%5 != 0:
#         l.append(i)
# print(l)

# simulating login system...
# user_base = {
#     "Darklord":"Fambro69"
# }

# def add_user(username,password):
#     user_base[username] = password

# def del_user(username):
#     user_base.pop(username)

# add_user("mayank",69)
# del_user("mayank")
# print(user_base)

# for i in range(1,4):
#     print(f"Attempted for login: {i} \nTotal attempt: 3")
#     usr_name = input("User Name: ")
#     passwd = input("Password: ")
#     if usr_name in user_base.keys() and user_base[usr_name] == passwd:
#         print("Access Granted!!")
#         print(f"Welcome back: {usr_name}")
#         break
#     if usr_name in user_base.keys() and user_base[usr_name] != passwd:
#         print("Incorrect password")
    
#     if not (usr_name in user_base.keys()):
#         print("User not found!!")
    
# Find common elements between two lists:
# l1 = [1,3,4,5,1,1,1]
# l2 = [7,3,45,1,1,1]

# common_elements = []
# for i in l1:

#     if i in l2 and i in common_elements:
#         continue
#     if i in l2:
#         common_elements.append(i)
# print(f"The common elements are: {common_elements}")

# Multiplication tale 1 to 10:
# number = int(input("Enter number for the table: "))
# for i in range(1,11):
#     print(f"{number} X {i} = {number*i}")

# Find the second largest number in the list: 
# l = [1,8,4,9,5,7]
# def second_lar():
#     i = l[0]
#     for item in l:
#         if i > item:
#             pass
#         else:
#             i = item
#     l.remove(i)
#     new_l = l
#     i = new_l[0]
#     for item in new_l:
#         if i > item:
#             pass
#         else:
#             i = item
#     print(i)

# second_lar()


"""
---                                                                      │
│                                                                                      │
│             **MODULE 1 — Core Foundations (skippable but do these 2)**               │
│                                                                                      │
│             1. `print(bool("False"))` — predict the output first, then run it. Why? 
The outcome of the the no 1 will be ture cause any value of srring is a value and it is true for the value and the False is  not being used as the pythons inbuild boolen it is being used as the string
 │
│             2. `"5" * 3` vs `5 * 3` — what's the difference and why?                 │
│ here in question no 2 in the first case there is a string 5 and it is multiplied by 3 which will multiply the string 3 times and in the second case there are 2 numbers which will be multiplied as any two integer number will be                                                 │
│             ---                                                                      │
│                                                                                      │
│             **MODULE 2 — Control Flow (do all of these)**                            │
│                                                                                      │
│             **Bugs to fix in your existing code:**                                   │
│                                                                                      │
│             1. **Nested range check (line 191-194)** — currently broken. A number    │
│ can't be in both 0-50 AND 50-100. Fix using `elif` or separate non-nested checks.    │
│                                                                                      │
│             2. **Second largest (line 415-434)** — `i = l[0]` stores the *value*,    │
│ not the *index*. Then `l[i]` uses that value as an index. Works by accident on your  │
│ test list. Fix it to use proper index tracking.                                      │
│                                                                                      │
│             3. **Guessing game (line 259-268)** — `random.randint()` is INSIDE the   │
│ loop, so the number changes every guess. Move it before `while True:`.               │
│                                                                                      │
│             4. **Fibonacci (line 316-334)** — works but relies on `insert(1,1)` hack │
│ at the end. Rewrite the loop so the series is generated naturally without that.      │
│                                                                                      │
│             5. **Factorial function (line 281-297)** — infinite loop bug. When `n == │
│ 0`, you reset `n = l` and `l = 1`, but the loop never breaks. The standalone version │
│ (line 270-279) is correct — use that approach.                                       │
│                                                                                      │
│             ---                                                                      │
│                                                                                      │
│             **Missing exercises to write new:**                                      │
│                                                                                      │
│             6. **Sum digits of a number** — e.g., input `1234` → output `10`         │
│ (1+2+3+4). Use a loop with `%` and `//`.                                             │
│                                                                                      │
│             7. **Check if string contains only digits** — e.g., `"12345"` → yes,     │
│ `"12a45"` → no. No `str.isallowed()` — use a loop.                                   │
│                                                                                      │
│             8. **Menu-driven program** — while loop that shows:                      │
│                - Press 1: do X                                                       │
│                - Press 2: do Y                                                       │
│                - Press 3: quit                                                       │
│                Keeps running until user picks quit. (This is the backbone of every   │
│ CLI app.)                                                                            │
│                                                                                      │
│             9. **Simple ATM System** — start with balance = 1000. Menu:              │
│                - Check balance                                                       │
│                - Deposit (add to balance)                                            │
│                - Withdraw (subtract, but don't allow if insufficient)                │
│                - Exit                                                                │
│                Uses while loop + if-elif. Combines everything you've learned.        │
│                                                                                      │
│             ---   
"""
# Sum digits of a number
# number = input("Enter the number: ")
# n = 0
# for i in number:
#     n = int(i) + n

# print(n)

# Check if string contains only digits
# string = input("Enter the string: ")
# print(string.isdigit())

# Menu-driven program (restraunt editon)

menu = """
1. momos
2. egg role
3. biryani
4. choumin              (press 'q' to quit)
5. chiken lolipon       (press 'rq' to place order)
6. Masala dosa
"""

# print(menu.capitalize())
# l = []
# while True:
#     order = input("Add the dish : ")
#     if order == "q":
#         break
#     if order == "rq":
#         print("Order placed ")
#         print(f'You ordered dish: {l}')
#         break

#     l.append(order)


# Simple ATM System
balance = 1000
commands = """
c --> check balance
d --> deposit amount
w --> withdraw amout
q --> quit interface
"""
print(commands)
while True:
    query = input("Enter the operrations: ")
    if query == "c":
        print(balance)
    elif query == "d":
        amout = int(input("Enter the amount to deposit: "))
        balance = balance + amout
        print(f"Amount {amout} was deposited to your account")
        print(f"Now the current balance: {balance}")
    elif query == "w":
        amount = int(input("Enter the amount to withdraw: "))
        if (balance - amount) < 100: 
            print("Cannot withdraw... The bank blance should be atlest 100 rs...")
        else:
            balance = balance - amount
            print(f"Amount {amount} was withdrawl from your account")
            print(f"Now the current balance: {balance}")
    elif query == "q":
        print("Shutting down the system interface.......:)\nLamo XD")
        break