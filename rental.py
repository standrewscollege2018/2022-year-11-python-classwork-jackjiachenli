# # # # # # # # # # # # # # # # 
#  Basic Car Rental Program!  #
# # # # # # # # # # # # # # # #

import time

# lists
cars = [['Suzuki Van', 2, ''], 
        ['Toyota Corolla', 4, ''], 
        ['Honda CRV', 4, ''], 
        ['Suzuki Swift', 4, ''], 
        ['Mitsubishi Airtrek', 4, ''], 
        ['Nissan DC Ute', 4, ''], 
        ['Toyata Previa', 7, ''], 
        ['Toyota Hi Ace', 12, ''], 
        ['Toyota Hi Ace', 12, '']]
booked = []

#loop
running = True
while running == True:
    print("Welcome to the University vehicle rental system")
    print("The vehicles are: ")
    if all([x[2] == "- Unavaliable" for x in cars]): # if all cars are booked, exit look to Daily Summary
        print("All the cars have been booked for today")
        break
        
    for index in range(0, len(cars)): # prints the list of cars
        print("{}. {} ({}) {}".format(index+1, cars[index][0], cars[index][1], cars[index][2]))

    ask_vehicle = True
    while ask_vehicle == True: # ask which vehicle they would want to book loop
        try:
            vehicle_number = input("Which vehicle would you like to book? ")
            if int(vehicle_number) == 0: # if vehicle_number is 0, exit ask_vehicle loop
                break   
            elif vehicle_number.isdigit(): # if vehicle_number is valid digit
                if int(vehicle_number) <= 9 and int(vehicle_number) > 0: # if vehicle_number is between 1-9
                    if cars[int(vehicle_number)-1][2] == "- Unavaliable": # if car is already booked
                        print("** This vehicle is already booked. Please choose another **")
                        continue
                    else: # if car is not booked
                        cars[int(vehicle_number)-1][2] = "- Unavaliable"
                        car = cars[int(vehicle_number)-1][0]
                        print(f"You have booked the {car}")
                        ask_vehicle = False
                else: 
                    print("Please book a valid car") # if vehicle_number is outside of the 1-9 range
            else:     
                print("Please enter a valid integer") # if the vehicle number is not an accepted integer
        except ValueError:
            print("Please enter a integer") # if input is not an integer
            
    if int(vehicle_number) == 0: # exits loop to Daily Summary
        break
    
    ask_name = True
    while ask_name == True: # ask what their name is loop
        name = input("What is your name?")
        if name.replace(" ", "").replace("-", "").isalpha(): # if name is valid
            booked.append([car, name])
            print(f"Thanks {name}")
            ask_name = False
        else: # if name isn't accepted
            print("Please enter a valid name")

# Daily Summary
print("Daily Summary")
if len(booked) == 0: # if no cars have been booked
    print("There are no cars booked today")
else: # if there are cars that have been booked
    for i in range(0, len(booked)):
        print("{} - {}".format(booked[i][0], booked[i][1])) # prints all vehicle booked + name formatted: Suzuki Van - John Doe


