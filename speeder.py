# lists
fines = []
amount = []

# print a welcome message
print("Welcome to the Speeders Fine Calculation system")
print ("")

# loop for all the loops
running = True
while running == True:
    
    ask_name = True # ask name loop
    while ask_name == True:
        name = input("Enter the name of the offender: ")
        if name == "John Smith" or name == "Helga Norman" or name == "Zach Conroy":
            print(f"** ALERT! There is an arrest warrant for {name} **")
            break
        elif name == "end":
            ask_name = False
        elif not name.strip(): # checks if input is empty space
            print("Please enter a valid name")
        elif not name.replace(' ','').isalpha(): # checks if name is a-z and allows spaces inbetween the words
            print("Please enter a valid name")
        else:
            break # exits loop if is valid name
            
    ask_speed_limit = True # ask speed limit loop
    if name == "end": # if name is 'end', skip this loop
        ask_speed_limit = False
    while ask_speed_limit == True:
        speed_limit = input("Enter the speed limit (in km/h): ") 
        if speed_limit.isdigit() and int(speed_limit) > 0: # checks if speed limit is a digit and greater than 0
            ask_speed_limit = False # stops loop
        else:
            print("Please enter a valid speed limit.")
    
    ask_speed = True # ask speed loop
    if name == "end": # if name is 'end', skip this loop
        ask_speed = False
    while ask_speed == True:
        speed = input("Enter the offenders speed: ")
        if speed.isdigit(): # checks if the speed limit is a integer
            ask_speed = False # stops loop
            
            # calculates how much needs to be fined
            if  0 < int(speed) - int(speed_limit) < 10: 
                print(f"{name} should be fined $30")
                fine = 30
                fines.append([name, fine])
                amount.append(30)
            elif 10 <= int(speed) - int(speed_limit) <= 19:
                print(f"{name} should be fined $80")
                fine = 80
                fines.append([name, fine])
                amount.append(80)
            elif 20 <= int(speed) - int(speed_limit) <= 29:
                print(f"{name} should be fined $130")
                fine = 130
                fines.append([name, fine])
                amount.append(130)
            elif int(speed) - int(speed_limit) > 29:
                print(f"{name} should be fined $180")
                fine = 180
                fines.append([name, fine])
                amount.append(180)
            else: # if offender is not speeding
                print("Offender isn't going over the speed limit.")
                fine = 0
                fines.append([name, fine])
                amount.append(0)
        else:
            print("Please enter a valid speed.") 
    if name == "end": # exits the loop for all loops for end of day summary
        break
    else: # if name is not end, restart the loop (from the very beginning)
        continue

# end of day summary - only comes here is name is 'end'
print("End of day summary")
print(f"Total number of fines charges: {len(fines)}")
print(f"Total amount fines charges: ${sum(amount)}")
for index in range(0, len(fines)):
    print("{}. {}: ${}".format(index+1, fines[index][0], fines[index][1])) # prints in the format '{Index}. {Name}: ${Fine}'
