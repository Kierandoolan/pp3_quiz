import colorama
from colorama import Fore
colorama.init(autoreset=True)

quiz_info = [
    {"question": "Q1. What is the Capital of Ireland:",
     "answers": {"A": "Galway",
                 "B": "Dublin",
                 "C": "Cork",
                 "D": "Galway"},
     "correct": "B"},
    {"question": "Q2. Who Created the Xbox:",
     "answers": {"A": "Sony",
                 "B": "Apple",
                 "C": "Nintendo",
                 "D": "Microsoft"},
     "correct": "D"},
    {"question": "Q3. Where is the Car manufacturers Audi From:",
     "answers": {"A": "Germany",
                 "B": "China",
                 "C": "USA",
                 "D": "London"},
     "correct": "A"},

    {"question": "Q4. Which of these is a Song from Red Hot Chilli Peppers:",
     "answers": {"A": "UpTown Girl",
                 "B": "Californation",
                 "C": "Adore You ",
                 "D": "Londons Burning"},
     "correct": "B"},
    {"question": "Q5. Which of these EU countries does not use the euro as\
 its currency?",
     "answers": {"A": "Poland",
                 "B": "Denmark",
                 "C": "Sweeden",
                 "D": "All of the Above"},
     "correct": "D"},
    {"question": "Q6. What color dresses do Chinese women traditionally wear on\
 their wedding day? ",
     "answers": {"A": "Blue",
                 "B": "Gold",
                 "C": "White",
                 "D": "Red"},
     "correct": "D"},
    {"question": "Q7. How many molecules of oxygen does ozone have?",
     "answers": {"A": "One",
                 "B": "Two",
                 "C": "Three",
                 "D": "Four"},
     "correct": "C"},
    {"question": "Q8. Where did the croissant originate?",
     "answers": {"A": "France",
                 "B": "Austria",
                 "C": "Turkey",
                 "D": "Tokyo"},
     "correct": "B"},
    {"question": "Q9. Pupusas are from what country",
     "answers": {"A": "Mexico",
                 "B": "El Salvador",
                 "C": "Brazil",
                 "D": "Poland"},
     "correct": "B"},
    {"question": "Final Question.  Which of these US presidents appeared on\
 the television series 'Laugh-In'  ",
     "answers": {"A": "Lyndon Johnson",
                 "B": "Richard Nixon",
                 "C": "Jimmy Carter",
                 "D": "Gerald Ford"},
     "correct": "B"},
]


def introduction():

    """
    Function to ask the user for name, explain what the game
    and to ask are they ready to begin the quiz
    """
    name = input("Please enter your name: \n")
    print(Fore.GREEN + " _____ _             ___        _     ")
    print(Fore.GREEN + "|_   _| |__   ___   / _ \ _   _(_)____")
    print(Fore.GREEN + "  | | | '_ \ / _ \ | | | | | | | |_  /")
    print(Fore.GREEN + "  | | | | | |  __/ | |_| | |_| | |/ / ")
    print(Fore.GREEN + "  |_| |_| |_|\___|  \__\_\\__,__|_/___|")
    print (f"Welcome to the Trivia Quiz {name} where we test your knowledge ")
    print ("There are 10 questions that gets harder with each\
 question answered,")
    print ("There are four choices for each question ")
    print ("Please Pick A, B, C or D when answering \n")

    start = True
    while start:
        answer = input(f"Are you ready to begin the quiz {name} Y/N :")
        if answer.upper() == "Y":
            print('Excellent! Lets Play the Quiz! \n')
            break
        elif answer.upper() == "N":
            print('Not ready. please press Y when ready.')
        else:
            print(Fore.RED + 'invalid')


def start_quiz(quiz_info):
    """
    Function to loop through all questions and possible answers
    when the user gets the answer correct 100euro is added to their score.
    I got aid from https://realpython.com/python-quiz-application/
    """
    cash = 0
    for info in quiz_info:
        answer = ''
        while answer not in ['A', 'B', 'C', 'D']:
            print(Fore.MAGENTA + f"{info['question']}")

            for key, value in info['answers'].items():
                print(Fore.CYAN + f"{key}: {value}")

            answer = input("What is your answer?\n")
            answer = answer.upper()

            if answer not in info['answers']:
                print(Fore.RED + "Invalid Choice. Please try again with the\
 correct letters \n")
        if answer == info['correct']:
            cash += 100
            print(Fore.GREEN + f"Well done thats the correct answer!\
 You gain {cash} euro \n")
        else:
            print(Fore.RED + " Oh No! Wrong answer. \n")

    end_of_quiz(cash)


def end_of_quiz(cash):
    """
    Function to tell the user of its overall score
    """
    if cash == 1000:
        print(Fore.YELLOW + f"Well done you got the top prize of {cash}euro.\
 Congraulations!")
    elif cash == 0:
        print(Fore.RED + f"Oh no you didn't get any questions right.\
 You have zero euro!")
    else:
        print(Fore.GREEN + f"Well done overall you have made {cash} euro.\
 Congraulations!")
    restart_game()


def restart_game():
    """
    Function to ask the user if they would like to restart the game
    or to finish the game
    """
    answer = input("Would you like to try and beat your score? Y/N: ")
    if answer.upper() == "Y":
        start_quiz(quiz_info)
    elif answer.upper() == "N":
        print("Thanks for Playing! Please come back again")
    else:
        print(Fore.RED + "Invalid Choice")
        restart_game()

introduction()
start_quiz(quiz_info)
