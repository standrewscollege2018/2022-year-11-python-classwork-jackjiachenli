import random
import time 

names = []

print("Hello there!")

ask_prize = True
while ask_prize == True:
    prize = str(input("What is the prize being raffled?"))
    if prize.isalpha():
        ask_prize = False
    else:
        print("Please enter a valid prize")

ask_value = True
while ask_value == True:
    try:
        value = int(input("What is the value of the prize?"))
        ask_value = False
    except ValueError:
        print("Please enter a valid integer")
    

ask = True
end = ("end")

while ask == True:
    name = str(input("Please enter the names that are being raffled, to stop, type end."))
    if name == end:
        print("Deciding winner...")
        time.sleep(1)
        print(f"The winner is {random.choice(names)}")
        ask = False
    elif name.isalpha():
        names.append(name)
    else:
        print("Please enter a valid name")