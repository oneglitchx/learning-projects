import random
import os
import json


choices = ["rock", "paper", "scissors"]
score_data = {}
# Define the computers randomized output
def computer_choices_function():
    global computer_suffled_choices
    computer_suffled_choices = random.choice(choices)
    # print(computer_suffled_choices)

# Take user input in a fuction
def user_input():
    user_prompt = input("Enter the options: ").lower()
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
    elif user_prompt == "rock" and computer_suffled_choices == "paper":
        return -1
    elif user_prompt == "paper" and computer_suffled_choices == "scissors":
        return -1
    elif user_prompt == "scissors" and computer_suffled_choices == "rock":
        return -1
    # Winning istances 
    elif user_prompt == "scissors" and computer_suffled_choices == "paper":
        return 1
    elif user_prompt == "paper" and computer_suffled_choices == "rock":
        return 1
    elif user_prompt == "rock" and computer_suffled_choices == "scissors":
        return 1
    
    
# Make a while loop to keep track the point scored in 1 round which consists of 10 or 5 chances 
def game():
    if not(os.path.exists("data.json")):
        with open("data.json", "w") as f:
            pass

    chances = 0
    welcome = "Welcome to the rock, paper and scissors game.".title().center(34,"~")
    print(welcome.center(45,"~"))
    result_of_game = []
    while True:
        computer_choices_function()
        if chances == 5:
            break
        user_option = user_input()
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
    with open("data.json","a") as f:
        json.dump(score_data,f,indent=4)
# write the score of the game json file with the date and time and the functionality to name the game instance score 

if __name__ == "__main__":
    game()
