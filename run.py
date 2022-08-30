"""
import section (get color)
"""


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
    {"question": "Q5. Which of these EU countries does not use the euro as its currency?",
     "answers": {"A": "Poland",
                 "B": "Denmark",
                 "C": "Sweeden",
		         "D": "All of the Above"},
     "correct": "D"},
    {"question": "Q6. What color dresses do Chinese women traditionally wear on their wedding day? ",
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
    {"question": "Final Question.  Which of these US presidents appeared on the television series 'Laugh-In'  ",
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

    print (f"Welcome to the Trivia Quiz {name} where we test your knowledge, \n")
    print ("There are 10 questions that gets harder with each question answered, \n")
    print ("There are four choices for each question \n")
    print ("Please Pick A, B, C or D when answering \n")

    start= True
    while start:
        answer = input(f"Are you ready to begin the quiz {name} Y/N :")

        if answer.upper() == "Y":
            
            print('Lets Play the Quiz!')
            break
        elif answer.upper() == "N":
            print('not ready')
        else :
            print('invalid')

def start_quiz(quiz_info):
    cash = 0
    for info in quiz_info:
        answer = ''
        while answer not in ['A', 'B', 'C', 'D']:
            print(f"{info['question']}")

            for key, value in info['answers'].items():
                print(f"{key}: {value}")

            answer = input("What is your answer?\n")
            answer = answer.upper()

            if answer not in info['answers']:
                print("Invalid Choice. Please try again with the correct letters\n")
        if answer == info['correct']:
            cash += 100
            print(f"Well done thats the correct answer ! You gain {cash} euro \n")
        else:
            print("Wrong answer.")



introduction()
start_quiz(quiz_info)
