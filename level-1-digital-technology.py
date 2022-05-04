""" This is a multi-choice quiz and is made by Jack Li """

import sqlite3

valid_answers = ["1", "2", "3", "4"]
correct_answers = []

DATABASE = "quiz.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()



def ask_continue():
    ask_resume = True
    while ask_resume == True:
        try:
            resume = int(input())
            if resume == 1:
                ask_resume = False
            elif resume == 2:
                ask_resume = False
                ask_quiz_number = True
            else:
                raise ValueError
        except ValueError:
            print("Please enter 1 or 2")

def print_quiz():
    for result in results:
        print(
            f"""
Question {result[0]}. {result[1]}
Is it:
1. {result[2]}
2. {result[3]}
3. {result[4]}
4. {result[5]}
"""
        )
        print("Please enter your answer as a number")
        ask_answer = True
        while ask_answer == True:
            answer = input()
            if answer == result[6]:
                print("correct")
                correct_answers.append(result[0])
                ask_answer = False
            elif answer != result[6] and answer in valid_answers:
                print(
                    f"""
Incorrect
The correct answer was {result[6]}"""
                )
                ask_answer = False
            else:
                print("Please enter a valid answer")


def get_percentage():
    length = cursor.fetchone()[0]
    percentage = 100 * len(correct_answers) / length
    print(
        f"""
You got {len(correct_answers)}/{length} correct
That is {percentage}% correct!"""
    )



print(
    """
Welcome to the multi-choice quiz
Lets start off with getting your name
"""
)
print("What is your name?")

name = input()

print(
    f"""
Hi {name}
What quiz would you like to choose?
1. Animals Quiz
2. Games Quiz
Please enter 1 or 2
"""
)

ask_quiz_number = True
while ask_quiz_number == True:
    try:
        print("What quiz would you like to do?")
        quiz_number = int(input())
        if int(quiz_number) == 1:
            ask_quiz_number = False
            print(
                """
You have selected the Animals Quiz
This quiz has 10 questions
Are you sure you want to continue?
            """
            )
            print("Type 1 to continue or 2 to return")
            ask_continue()

        elif int(quiz_number) == 2:
            ask_quiz_number = False
            print(
                """
You have selected the Games Quiz
This quiz has 10 questions
Are you sure you want to continue?
            """
            )
            print("Type 1 to continue or 2 to return")
            ask_continue()
        else:
            raise ValueError
    except ValueError:
        print("Please enter a valid quiz number")

if quiz_number == 1:
    results = cursor.execute("SELECT * FROM animals")
    print_quiz()
    cursor.execute("SELECT question_id FROM animals ORDER BY question_id DESC LIMIT 1")
    get_percentage()
elif quiz_number == 2:
    results = cursor.execute("SELECT * FROM games")
    print_quiz()
    cursor.execute("SELECT question_id FROM games ORDER BY question_id DESC LIMIT 1")
    get_percentage()
