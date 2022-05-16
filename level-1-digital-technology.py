""" This is a multi-choice quiz and is made by Jack Li """

# imports
import sqlite3

# lists
valid_answers = ["1", "2", "3", "4"]
correct_answers = []

# connect to the database
DATABASE = "quiz.db"
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# functions
def ask_continue():
    global ask_number
    print("Type 1 to continue or 2 to return")
    # asks whether the user wants to continue or go back to the selection menu
    ask_resume = True
    while ask_resume == True:
        try:
            resume = int(input())
            if resume == 1:
                ask_resume = False
            elif resume == 2:
                ask_resume = False
                ask_number = True
            else:
                raise ValueError
        except ValueError:
            print("Please enter 1 or 2")


def print_quiz():
    # for loop to print out the questions
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
        # asks the user for an input of their chosen answer
        ask_answer = True
        while ask_answer == True:
            try:
                answer = input()
                # checks if the users answer is correct
                if int(answer) == result[6]:
                    print("Correct")
                    correct_answers.append(result[0])
                    ask_answer = False
                elif answer != result[6] and answer in valid_answers:
                    print(
                        f"""
Incorrect
The correct answer was {result[6]} - {result[result[6]+1]}
                    """
                    )
                    ask_answer = False
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid answer")


def get_percentage():
    global name
    global store_quiz_name
    # fetches the first result (which is the length of the quiz)
    length = cursor.fetchone()[0]
    fraction = f"{len(correct_answers)}/{length}"
    percentage = round(100 * len(correct_answers) / length, 1)
    points = 100
    score = points * len(correct_answers)
    # inserts the users score into the database
    cursor.execute(
        "INSERT INTO leaderboards (name, score, quiz_name) VALUES (?, ?, ?)", (name, score, store_quiz_name)
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
    # asks whether the user wants to return to the selection menu
    ask_return = True
    while ask_return == True:
        try:
            restart = int(input())
            if restart == 1:
                running = True
                correct_answers = []
                ask_return = False
            elif restart == 2:
                running = False
                ask_return = False
            else:
                raise ValueError
        except ValueError:
            print("Please enter 1 or 2")

# start of program
print(
    """
Welcome to the multi-choice quiz
Lets start off with getting your name
"""
)

print("What is your name?")

# gets the users name
ask_name = True
while ask_name == True:
    try:
        name = input()
        if name.isalpha() == True or name.isdigit() == True:
            ask_name = False
        else:
            raise ValueError
    except ValueError:
        print("Please enter a valid name")

# while loop
running = True
while running == True:
    # ask what number they would like to choose
    ask_number = True
    while ask_number == True:
        print(
        f"""
Hi {name}
Please pick a number
1. Animals Quiz
2. Games Quiz
3. Score Leaderboards
4. Quit
Please enter 1, 2, 3 or 4
    """
        )
        try:
            print("What number will you pick?")
            number = int(input())
            if int(number) == 1:
                ask_number = False
                cursor.execute("SELECT question_id FROM animals ORDER BY question_id DESC LIMIT 1")
                length = cursor.fetchone()[0]
                print(
                    f"""
You have selected the Animals Quiz
This quiz has {length} questions
Are you sure you want to continue?
                """
                )
                ask_continue()
            elif int(number) == 2:
                ask_number = False
                cursor.execute("SELECT question_id FROM animals ORDER BY question_id DESC LIMIT 1")
                length = cursor.fetchone()[0]
                print(
                    f"""
You have selected the Games Quiz
This quiz has {length} questions
Are you sure you want to continue?
                """
                )
                ask_continue()
            elif int(number) == 3:
                ask_number = False
                print(
                    """
You have selected the Score Leaderboards
Are you sure you want to continue?
                """
                )
                ask_continue()
            elif int(number) == 4:
                ask_number = False
                print(
                    """
You have selected to quit
Are you sure you want to continue?
                """
                )
                ask_continue()
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid quiz number")

    # if they picked animals quiz
    if number == 1:
        store_quiz_name = "Animals Quiz"
        results = cursor.execute("SELECT * FROM animals")
        print_quiz()
        # selects the highest question_id from the games database
        cursor.execute("SELECT question_id FROM animals ORDER BY question_id DESC LIMIT 1")
        get_percentage()
        ask_restart()
    # if they picked the games quiz
    elif number == 2:
        store_quiz_name = "Games Quiz"
        results = cursor.execute("SELECT * FROM games")
        print_quiz()
        # selects the highest question_id from the games database
        cursor.execute("SELECT question_id FROM games ORDER BY question_id DESC LIMIT 1")
        get_percentage()
        ask_restart()
    # if they picked to see the leaderboards
    elif number == 3:
        # selects the name and the score from the leaderboards table then sorts it by score and adds a row number which will act as a ranking system and is limited to the top 5
        results = cursor.execute("SELECT name, score, quiz_name, ROW_NUMBER() OVER (ORDER BY score DESC) AS rank FROM leaderboards LIMIT 5")
        # prints the top 5 scores
        for result in results:
            print(
                f"""
{result[3]}. {result[0]} - {result[1]} points - {result[2]}"""
            )
    elif number == 4:
        running = False
