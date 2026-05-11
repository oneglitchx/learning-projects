import random
import os
import json
import time

current_time = time.strftime("%Y-%m-%A %H:%M:%S")
print(current_time)
choices = ["rock", "paper", "scissors"]
data = {}
score_data = {}
# Define the computers randomized output
def computer_choices_function():
    global computer_suffled_choices
    computer_suffled_choices = random.choice(choices)
    # print(computer_suffled_choices)

# Take user input in a fuction
def user_input():
    user_prompt = input("Enter the options: (press 'q' to quit or 'l' to list score)").lower()
    if user_prompt == 'q':
        return "q"
    elif user_prompt == "l":
        return "l"
    if not(user_prompt in choices):
        print("This program only accepts: (rock, paper and scissors) as input")
        return None
    return user_prompt
    
# Make the simple logic for the win, loose and draw 
def core_logic(user_prompt):
    # Instance of draw 
    if user_prompt == computer_suffled_choices:
        return 0
    # Instance of loseing
    elif (user_prompt == "rock" and computer_suffled_choices == "paper") or (user_prompt == "paper" and computer_suffled_choices == "scissors") or (user_prompt == "scissors" and computer_suffled_choices == "rock"):
        return -1
    # Winning istances 
    elif (user_prompt == "scissors" and computer_suffled_choices == "paper") or (user_prompt == "paper" and computer_suffled_choices == "rock") or (user_prompt == "rock" and computer_suffled_choices == "scissors"):
        return 1

# To see the score of the game
def see_score():
    with open('data.json',"r") as f:
        conDict = json.load(f)
        dates = list(conDict.keys())
        scores = list(conDict.values())
        # print(scores[i])
    
        print("The scores of the game".center(45,"~"))
        for i in range(0,len(dates)):
            print(f"The date: {dates[i]}")
            keys_real_attempts = list(scores[i].keys())
            values_real_attempts = list(scores[i].values())
            for i in range(0,len(keys_real_attempts)):
                print(f"{keys_real_attempts[i]} attempt: {values_real_attempts[i]}")


# Make a while loop to keep track the point scored in 1 round which consists of 10 or 5 chances 
def game():
    if not(os.path.exists("data.json")):
        with open("data.json", "w") as f:
            a = {}
            json.dump(a,f)

    chances = 0
    welcome = "Welcome to the rock, paper and scissors game.".title().center(34,"~")
    print(welcome.center(45,"~"))
    result_of_game = []
    while True:
        computer_choices_function()
        if chances == 5:
            break
        user_option = user_input()
        if user_option == "q":
            break
        elif user_option == "l":
            see_score()

        if not(user_option == None):
            chances += 1
        else:
            continue
        return_value = core_logic(user_option)
        result_of_game.append(return_value)
        
        if return_value == 0:
            print("Draw!!")
            score_data[chances] = "draw"
        elif return_value == 1:
            print("You Won!!")
            score_data[chances] = "won"
        elif return_value == -1:
            print("You lose!")
            score_data[chances] = "lose"

    number_win = result_of_game.count(1)
    number_lose = result_of_game.count(-1)
    number_draw = result_of_game.count(0)
    print(f"you won: {number_win} times\nyou lose: {number_lose} times and\nthe game was draw for {number_draw} times.".title())
    # To write the data to json
    with open("data.json","r") as f:
        data_game_contants = json.load(f)
        data = data_game_contants
    with open("data.json","w") as f:
        data[current_time] = score_data 
        json.dump(data,f,indent=4)


if __name__ == "__main__":
    game()
