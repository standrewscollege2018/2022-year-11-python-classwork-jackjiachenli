# import
import time

# vars and lists
opponents = []
points = []
wait = 0.5

# ask for team name loop
print("Hello there!")
time.sleep(wait)
ask_team_name = True
while ask_team_name == True:
    team = input("What is the name of the team competing?")
    if not team.strip():
        print("Please enter a valid team name")
    else:
        ask_team_name = False

# ask for opponent names loop
done = ("done")
time.sleep(wait)
ask_opponents = True
while ask_opponents == True:
    opponent = input("What are the names of the opponents? To stop, type 'done'")
    if opponent == done: 
        ask_opponents = False
    elif not opponent.strip():
        print("Please enter a valid team name")
    else:
        opponents.append(opponent)

# interval
time.sleep(wait)
print("Thank you for entering the team names, we will now move onto scoring.")
time.sleep(wait)
print("Please enter the score like: 5-3 with the friendly team's score first.")
time.sleep(wait)

# ask score loop
ask_score = True
for i in range(0, len(opponents), 1):
    while ask_score == True:
        try:
            score_1, score_2 = input(f"What was the score against {opponents[i]}?").split("-")
            if int(score_1) < 0 or int(score_2) < 0 or type(score_1) == str or type(score_2) == str:
                print("Please enter a valid score.")
            elif score_1 > score_2:
                points.append(3)
            elif score_1 < score_2:
                points.append(1)
            else:
                points.append(2)
        except ValueError:
            print("Please enter a valid score.")   

# print the sum of points
print(f"The total amount of points that {team} earned is {sum(points)}")
    