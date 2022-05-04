""" This is a multi-choice quiz and is made by Jack Li """

import sqlite3

DATABASE = "quiz.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

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
Type 1 to continue or 2 to return
            """
            )
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

        elif int(quiz_number) == 2:
            ask_quiz_number = False
            print(
                """
You have selected the Games Quiz
This quiz has 10 questions
Are you sure you want to continue?
Type 1 to continue or 2 to return
            """
            )
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
        else:
            raise ValueError
    except ValueError:
        print("Please enter a valid quiz number")
