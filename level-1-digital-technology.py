""" This is a multi-choice quiz and is made by Jack Li """

import sqlite3

valid_answers = ["1", "2", "3", "4"]
correct_answers = []

DATABASE = "quiz.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()


def ask_continue():
    global ask_quiz_number
    print("Type 1 to continue or 2 to return")
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
            try:
                answer = input()
                if int(answer) == result[6]:
                    print("correct")
                    correct_answers.append(result[0])
                    ask_answer = False
                elif answer != result[6] and answer in valid_answers:
                    print(
                        f"""
Incorrects
The correct answer was {result[6]}
    """
                    )
                    ask_answer = False
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid answer")


def get_percentage():
    global name
    length = cursor.fetchone()[0]
    fraction = f"{len(correct_answers)}/{length}"
    percentage = round(100 * len(correct_answers) / length, 1)
    score = 100 * len(correct_answers)
    cursor.execute(
        "INSERT INTO leaderboards (name, score) VALUES (?, ?)", (name, score)
    )
    connection.commit()
    print(
        f"""
You got {fraction} correct
That is {percentage}% correct!
You got a score of {score}!
    """
    )


def ask_restart():
    global running
    global correct_answers
    print(
        """
Do you want to return to the start or quit?
Type 1 to return, 2 to quit
    """
    )
    try:
        ask_return = int(input())
        if ask_return == 1:
            running = True
            correct_answers = []
        elif ask_return == 2:
            running = False
    except ValueError:
        print("Please enter 1 or 2")


print(
    """
Welcome to the multi-choice quiz
Lets start off with getting your name
"""
)
print("What is your name?")

name = input()

running = True
while running == True:
    print(
        f"""
Hi {name}
Please pick a number
1. Animals Quiz
2. Games Quiz
3. Score Leaderboards
Please enter 1, 2 or 3
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
                ask_continue()
            elif int(quiz_number) == 3:
                ask_quiz_number = False
                print(
                    """
You have selected the Score Leaderboards
Are you sure you want to continue?
                """
                )
                ask_continue()
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid quiz number")

    if quiz_number == 1:
        results = cursor.execute("SELECT * FROM animals")
        print_quiz()
        cursor.execute(
            "SELECT question_id FROM animals ORDER BY question_id DESC LIMIT 1"
        )
        get_percentage()
        ask_restart()
    elif quiz_number == 2:
        results = cursor.execute("SELECT * FROM games")
        print_quiz()
        cursor.execute(
            "SELECT question_id FROM games ORDER BY question_id DESC LIMIT 1"
        )
        get_percentage()
        ask_restart()
    elif quiz_number == 3:
        results = cursor.execute(
            "SELECT name, score, ROW_NUMBER() OVER ( ORDER BY score DESC) AS rank FROM leaderboards LIMIT 5"
        )
        for result in results:
            print(
                f"""
{result[2]}. {result[0]} {result[1]}
            """
            )
