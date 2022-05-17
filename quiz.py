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
    # asks whether the user wants to continue or go back to the selection menu
    ask_resume = True
    while ask_resume == True:
        try:
            resume = int(input())
            if resume == 1:
                ask_resume = False
                return True
            elif resume == 2:
                ask_resume = False
                return False
            else:
                raise ValueError
        except ValueError:
            print("Please enter 1 or 2")

def print_quiz():
    correct_answers = []
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
    cursor.execute(
        "INSERT INTO leaderboards (name, score, quiz_name) VALUES (?, ?, ?)", (name, 100 * len(correct_answers), store_quiz_name)
    )
    connection.commit()
    print(
        f"""
You got {len(correct_answers)}/{length} correct
That is {round(100 * len(correct_answers) / length, 1)}% correct!
You got a score of {100 * len(correct_answers)}!
    """
    )

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
        try:
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
            print("What number will you pick?")
            number = int(input())
            if number == 1 or number == 2:
                if number == 1:
                    quiz = "animals"
                    store_quiz_name = "Animals Quiz"
                else:
                    quiz = "games"
                    store_quiz_name = "Games Quiz"
                cursor.execute(f"SELECT * FROM {quiz}")
                results = cursor.fetchall()
                length = len(results)
                print(f"{store_quiz_name} has {length} questions. Are you sure?")
                print("Type 1 to continue or 2 to return")
                if ask_continue():
                    ask_number = False
                    print_quiz()
                else:
                    continue
            elif number == 3:
                print("You have selected to see the leaderboards")
                print("Type 1 to continue or 2 to return")
                if ask_continue():
                    cursor.execute("SELECT name, score, quiz_name, ROW_NUMBER() OVER (ORDER BY score DESC) AS rank FROM leaderboards LIMIT 5")
                    results = cursor.fetchall()
                    print("")
                    for result in results:
                        print(f"{result[3]}. {result[0]} - {result[1]} points - {result[2]}")
                else:
                    continue
            elif number == 4:
                print("You have selected to quit the program")
                print("Type 1 to continue or 2 to return")
                if ask_continue():
                    ask_number = False
                    running = False
        except ValueError:
            print("Please enter a valid quiz number")
