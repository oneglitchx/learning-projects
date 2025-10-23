# Terminal asthetics 
def welcome():
    print("welcome to the calculator".title().center(40,"~"))
    print("this calculator taskes two numbers and an operator as inputs and performs various operations upon them".title())




# Taking user inputs for the numbers and the operator
def inputs():
    number1 = int(input("enter the first number: ".title()))
    operation = input("enter the operator: ".title())
    number2 = int(input("enter the second number: ".title()))
    return number1, operation, number2
    
    
# Operation on the numbers 
def logic(number1 , operation, number2):
    if operation == "+":
        print(f"the sum of {number1} and {number2} is {number1 + number2}".title())
    elif operation == "-":
        print(f"the difference of {number1} and {number2} is {number1 - number2}".title())
    elif operation == "*":
        print(f"the multiplication of {number1} and {number2} is {number1 * number2}".title())
    elif operation == "/":
        print(f"the division of {number1} by {number2} is {number1 / number2}".title())
    elif operation == "//":
        print(f"the round off quotient of {number1} divided by {number2} is {number1 // number2}".title())
    elif operation == "%":
        print(f"the remainder of {number1} divided by {number2} is {number1 % number2}".title())
    elif operation == "**":
        print(f"the number {number1} raised to the power to {number2} is {number1 ** number2}".title())
    else:
        print("this calculator only supports (+ 'addition',- 'subtraction',* 'multiplication',/ 'division',// 'floor division',% 'modulo',** 'exponent')".title())
# Output for the result

welcome()
num1, ope , num2 = inputs()
logic(num1, ope , num2)

""" 
The return keyword in functions with multiple variables gives a tuple and the function itself
acts as a variable to store it.
"""