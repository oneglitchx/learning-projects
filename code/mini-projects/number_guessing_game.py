import random

computer_random_number = random.randint(1,100)

iteration = 0
while True:
    iteration += 1
    try:
        user_number = int(input("Enter the number: "))
    except:
        print("The user input should only be an integer.")
        iteration -= 1
    if user_number > computer_random_number:
        print("Lower number please!!!")
    elif user_number < computer_random_number:
        print("Higher number please!!!")
    else:
        if user_number == computer_random_number:
            print(f"You gusses the number right in in {iteration} turns.")
            break