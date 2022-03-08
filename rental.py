# # # # # # # # # # # # # # # # 
#  Basic Car Rental Program!  #
# # # # # # # # # # # # # # # #

import time

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

running = True
while running == True:
    print("Welcome to the University vehicle rental system")
    print("The vehicles are: ")
    if all([x[2] == "- Unavaliable" for x in cars]):
        print("All the cars have been booked for today")
        break
        
    for index in range(0, len(cars)):
        print("{}. {} ({}) {}".format(index+1, cars[index][0], cars[index][1], cars[index][2]))
        
    ask_vehicle = True
    while ask_vehicle == True:
        try:
            vehicle_number = input("Which vehicle would you like to book? ")
            print("You may enter 0 to end the day.")
            if int(vehicle_number) == 0:
                break   
            elif vehicle_number.isdigit or vehicle_number.replace('-','').isdigit():
                if int(vehicle_number) <= 9 and int(vehicle_number) > 0:
                    if cars[int(vehicle_number)-1][2] == "- Unavaliable":
                        print("** This vehicle is already booked. Please choose another **")
                        continue
                    else:
                        cars[int(vehicle_number)-1][2] = "- Unavaliable"
                        car = cars[int(vehicle_number)-1][0]
                        print(f"You have booked the {car}")
                        ask_vehicle = False
                else:
                    print("Please book a valid car")
            else:     
                print("Please enter a valid integer")
        except ValueError:
            print("Please enter a integer")
            
    if int(vehicle_number) == 0:
        break
    
    ask_name = True
    while ask_name == True:
        name = input("What is your name?")
        if name.replace(" ", "").replace("-", "").isalpha():
            booked.append([car, name])
            print(f"Thanks {name}")
            ask_name = False
        else:
            print("Please enter a valid name")

print("Daily Summary")
if len(booked) == 0:
    print("There are no cars booked today")
else:
    for i in range(0, len(booked)):
        print("{} - {}".format(booked[i][0], booked[i][1]))


