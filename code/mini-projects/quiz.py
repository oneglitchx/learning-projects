import os
import json

# file to save the questions and their options and correct answers

def exists_quiz_file():
    if not(os.path.exists("quiz.json")):
        with open("quiz.json", "w") as f:
            a = {}
            json.dump(a,f)
    else:
        with open("quiz.json",'r') as f:
            contant = f.read()
        if contant == "":
            with open("quiz.json", "w") as f:
                a = {}
                json.dump(a,f)

# For adding questions
def addQuestions():
    with open("quiz.json","r") as f:
        main_dict = json.load(f)
    # print(main_dict)

    question_input = input("Enter the questions you want to add to your quiz: ")
    option_inputs = input("Enter the options fo the questions: ")
    right_answer = input("Enter the right option to the question: ")
    list_Options = option_inputs.split(",")
    print(list_Options)
    index_of_question = len(main_dict)+1 
    main_dict[index_of_question] = {"question":question_input,"options":list_Options,"answer": right_answer}
    print(main_dict)
    with open("quiz.json","w") as f:
        json.dump(main_dict,f,indent=4)


def printAllQuestions():
    with open('quiz.json',"r") as f:
        global dictionary_of_questions
        dictionary_of_questions = json.load(f)
    
    for index, i in enumerate(dictionary_of_questions):
        single_question = dictionary_of_questions.get(i).get("question")
        a, b, c, d = list(dictionary_of_questions.get(i).get("options"))

        format = f"Q. {index + 1} {single_question}\nOptions:\na. {a} \nb. {b}\nc. {c}\nd. {d}"
        print(format)

def takeQuiz():
    with open('quiz.json',"r") as f:
        dictionary_of_questions = json.load(f)
    
    correct_answer = 0
    for index, i in enumerate(dictionary_of_questions):
        single_question = dictionary_of_questions.get(i).get("question")
        a, b, c, d = list(dictionary_of_questions.get(i).get("options"))

        format = f"Q. {index + 1} {single_question}\nOptions:\na. {a} \nb. {b}\nc. {c}\nd. {d}"
        print(format)
        answer = input("Enter the answer to the question: ")
        if answer == dictionary_of_questions.get(i).get("answer"):
            print("Correct Answer 🎉\n")
            correct_answer += 1
        else:
            print("Wrong Answer 😢\n")    
    print("The quiz is over dude!".title().center(45,"~"))
    print(f"Total question: {len(dictionary_of_questions)}\nCorrect: {correct_answer}\nWrong: {(len(dictionary_of_questions)) - correct_answer}\n")


def delQuestion():
    printAllQuestions()
    ask = (input("Which question you want to delete?: "))
    dictionary_of_questions.pop(ask)
    print(f"Question number {ask} is deleted.")
    new_dict_of_questions = {}
    index = 1
    for i in sorted(dictionary_of_questions.keys()):
        new_dict_of_questions[index] = dictionary_of_questions.get(i)
        index += 1 
    
    with open("quiz.json", 'w') as f:
        json.dump(new_dict_of_questions,f,indent=4)

def main():
    # delete the qustions 
    
    exists_quiz_file()   # check whither the quiz json file exist or not, if not make one
    greeting = "welcome to the quiz game".title().center(100,"~")
    print(f"{greeting}")
    instructions = """
    These are the all the commands and their functions:
        list --> to see all the questions
        add --> to new add questions
        del --> to delete specific questions
        quiz --> to take the whole quize 
        q --> to exit the program 
        / --> to see all the commands
    """
    print(instructions)
    command_list = "list add del quiz q / clear".split(" ")
    print(command_list)

    while True:
        command = input(f"Enter a command to proceed: ")
        if not(command in command_list): 
            print("please enter a valid command!!!!!!!".upper())
        elif command == "q":
            print("Exiting quiz........")
            break
        elif command == "/":
            print(instructions)
        elif command == "list":
            printAllQuestions()
        elif command == "clear":
            os.system("clear")
        elif command == "add":
            addQuestions()
        elif command == "quiz":
            takeQuiz()
        elif command == "del":
            delQuestion()

        

main()