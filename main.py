import random
from re import T
from source.warehouse import *
from source.item import *
from source.shelf import *
from source.risk import *
from source.UI import *
from importexport import *


time_modifier = 0.1

item_risks = [["Fragile", "moving", 0.15, 20]]      #name, itype, probability, magnitude (seconds)
global_risks = [["Missplace", "handeling", 0.1, 10], ["Scanning Error", "scanning", 0.1, 5]]


def main():
    switch = True
    ui = UI()
    wh = warehouse()
    
    while switch:                   #Main UI loop
        print(ui.UI(0, None))
        user_input = input(":")
        # Warehouse Sim 0.1 

        # 1. Create Warehouse
        # 2. Manage Warehouse
        # 3. View Warehouse
        # 4. Simulate
        # 0. Exit

        if (user_input == "1"):
            while switch:
                print(ui.UI(1, None))
                user_input = input(":")

                # Create Warehouse:

                # 1. Create workers
                # 2. Create Arrivals
                # 3. Create Shelf
                # 4. Manage Items
                # 5. Average item time on shelves
                # 6. Create
                # 0. Back

                
                if (user_input == "1"):
                    while switch:
                    #Create workers:

                    # 1. Create multiple workers
                    # 2. Create single worker
                    # 0. Back   
                    
                        print(ui.UI(2,None))
                        user_input = input(":")

                        if user_input == "1":
                            # Create multiple workers:

                            # 1. Amount: {0}
                            # 2. Scan time: {1}
                            # 3. Walking Speed: {2}
                            # 4. Item handeling speed: {3}
                            # 5. Create.
                            # 0. Back
                            options = [-1,-1,-1,-1]
                            

                            while switch:                           #Checks if user input is valid and if so, 
                                print(ui.UI(3,options))             #inserts it into the class
                                user_input = input(":")
                                if user_input == "1":
                                    while switch:
                                        inval = input("Amount: ")
                                        if inval.isnumeric():
                                            options[0] = int(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                        
                                elif user_input == "2":
                                    while switch:
                                        inval = input("Scan Time: ")
                                        if inval.isnumeric():
                                            options[1] = int(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "3":
                                    while switch:
                                        inval = input("Walking Speed: ")
                                        if inval.isnumeric():
                                            options[2] = int(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "4":
                                    while switch:
                                        inval = input("Item handeling speed: ")
                                        if inval.isnumeric():
                                            options[3] = int(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "5":
                                    if (-1 not in options):
                                        wh.create_worker_lst(options[0], options[1], options[2], options[3])
                                        options = [-1,-1,-1,-1]
                                        print("Done")
                                    else:
                                        print("Invalid")
                                    
                                elif user_input == "0":
                                    switch = False
                                else:
                                    print("Invalid Input")
                            switch = True 
                                

                        elif user_input == "2":

                            # Create single worker

                            # 1. Scan time: {0}
                            # 2. Walking Speed: {1}
                            # 3. Item handeling speed: {2}
                            # 4. Create.
                            # 0. Back
                            options = [-1,-1,-1]
                            

                            while switch:
                                print(ui.UI(4,options))
                                user_input = input(":")
                                        
                                if user_input == "1":
                                    while switch:
                                        inval = input("Scan Time: ")
                                        if inval.isnumeric():
                                            options[0] = int(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "2":
                                    while switch:
                                        inval = input("Walking Speed: ")
                                        if inval.isnumeric():
                                            options[1] = int(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "3":
                                    while switch:
                                        inval = input("Item handeling speed: ")
                                        if inval.isnumeric():
                                            options[2] = int(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "4":
                                    if (-1 not in options):
                                        wh.create_worker_lst(1, options[0], options[1], options[2])
                                        options = [-1,-1,-1]
                                        print("Done")
                                    else:
                                        print("Invalid")
                                    
                                elif user_input == "0":
                                    switch = False
                                else:
                                    print("Invalid Input")
                            switch = True 

                        elif user_input == "0":
                            switch = False
                        else:
                            print("Invalid Input")
                    switch = True
                    

                elif (user_input == "2"):
                    # Create Arrivals and Departures

                    # 1. Arrivals capacity: {0}
                    # 2. Create
                    # 0. Back
                    options = [-1]

                    while switch:
                        print(ui.UI(5, options))
                        user_input = input(":")

                        if user_input == "1":
                            while switch:
                                inval = input("Arrivals capacity: ")
                                if inval.isnumeric():
                                    options[0] = int(inval)
                                    switch = False
                                else:
                                    print("Invalid")
                            switch = True
                        elif user_input == "2":
                            if -1 not in options:
                                wh.create_arrivals(options[0])
                                wh.create_departures()
                                print("Done")
                        elif user_input == "0":
                            switch = False
                        else:
                            print("Invalid")
                    switch = True


                elif (user_input == "3"):
                    # Create Shelf

                    # 1. Shelf capacity: {0}
                    # 2. Distance from arrivals: {1}
                    # 3. Distance from departures: {2}
                    # 4. Shelf Size: {3}
                    # 5. Create.
                    # 0. Back

                    options = [-1, -1, -1]

                    while switch:
                        print(ui.UI(6, options))
                        user_input = input(":")

                        if user_input == "1":
                            while switch:
                                inval = input("Shelf capacity: ")
                                if inval.isnumeric():
                                    options[0] = int(inval)
                                    switch = False
                                else:
                                    print("Invalid")
                            switch = True
                        elif user_input == "2":
                            while switch:
                                inval = input("Distance from arrivals: ")
                                if inval.isnumeric():
                                    options[1] = int(inval)
                                    switch = False
                                else:
                                    print("Invalid")
                            switch = True

                        elif user_input == "3":
                            while switch:
                                inval = input("Distance from departures: ")
                                if inval.isnumeric():
                                    options[2] = int(inval)
                                    switch = False
                                else:
                                    print("Invalid")
                            switch = True

                        elif user_input == "4":
                            if -1 not in options:
                                wh.create_shelf(options[0], options[1], options[2])
                                options[1] = -1
                                options[2] = -1
                                print("Done")
                        elif user_input == "0":
                            switch = False
                        else:
                            print("Invalid")
                    switch = True


                elif (user_input == "4"):
                    # Manage Items

                    # 1. Create scanning risks
                    # 2. Create moving risks
                    # 3. Create handeling risks
                    # 0. Back
                    

                    while switch:
                        print(ui.UI(7, None))
                        user_input = input(":")

                        if user_input == "1":
                            options = [-1, -1, -1, -1]
                            options[0] = "scanning risks"
                            while switch:
                                print(ui.UI(8, options))
                                user_input = input(":")

                                if user_input == "1":
                                    while switch:
                                        inval = input("Name: ")
                                        if inval != "":
                                            options[1] = inval
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "2":
                                    while switch:
                                        inval = input("Probability: ")
                                        if inval.isnumeric():
                                            options[2] = float(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "3":
                                    while switch:
                                        inval = input("Time penalty: ")
                                        if inval.isnumeric():
                                            options[3] = int(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "4":
                                    if -1 not in options:
                                        wh.item_risks.append(risk(options[1], "scanning", options[2], options[3]))
                                        print("Done")
                                    else:
                                        print("Fill all options")
                                elif user_input == "0":
                                    switch = False

                            switch = True

                        elif user_input == "2":
                            options = [-1, -1, -1, -1]
                            options[0] = "moving risks"
                            while switch:
                                # Create {0}

                                # 1. Name: {1}
                                # 2. Probability: {2}
                                # 3. Time penalty:  {3}
                                # 4. Create
                                # 0. Back.
                                print(ui.UI(8, options))
                                user_input = input(":")

                                if user_input == "1":
                                    while switch:
                                        inval = input("Name: ")
                                        if inval != "":
                                            options[1] = inval
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "2":
                                    while switch:
                                        inval = input("Probability: ")
                                        if inval.isnumeric():
                                            options[2] = float(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "3":
                                    while switch:
                                        inval = input("Time penalty: ")
                                        if inval.isnumeric():
                                            options[3] = int(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "4":
                                    if -1 not in options:
                                        wh.item_risks.append(risk(options[1], "moving", options[2], options[3]))
                                        print("Done")
                                    else:
                                        print("Fill all options")
                                elif user_input == "0":
                                    switch = False

                            switch = True

                        elif user_input == "3":
                            options = [-1, -1, -1, -1]
                            options[0] = "handeling risks"
                            while switch:
                                print(ui.UI(8, options))
                                user_input = input(":")

                                if user_input == "1":
                                    while switch:
                                        inval = input("Name: ")
                                        if inval != "":
                                            options[1] = inval
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "2":
                                    while switch:
                                        inval = input("Probability: ")
                                        if inval.isnumeric():
                                            options[2] = float(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "3":
                                    while switch:
                                        inval = input("Time penalty: ")
                                        if inval.isnumeric():
                                            options[3] = int(inval)
                                            switch = False
                                        else:
                                            print("Invalid")
                                    switch = True
                                elif user_input == "4":
                                    if -1 not in options:
                                        wh.item_risks.append(risk(options[1], "handeling", options[2], options[3]))
                                        print("Done")
                                    else:
                                        print("Fill all options")
                                elif user_input == "0":
                                    switch = False

                            switch = True

                        elif user_input == "0":
                            switch = False
                        else:
                            print("Invalid")

                    switch = True


                elif (user_input == "5"):
                    while switch:
                        options = [-1]
                        # Time precision.

                        # 1. Set time precision {0}
                        # 0. Back
                        print(ui.UI(9, options))
                        user_input = input(":")

                        if user_input == "1":
                            while switch:
                                inval = input("Shelf time: ")
                                if inval.isnumeric():
                                    options[0] = float(inval)
                                    switch = False
                                    wh.avg_shelfed = options[0]
                                    print("Done")
                                else:
                                    print("Invalid")
                            switch = True
                                
                        elif user_input == "0":
                            switch = False

                    switch = True


                elif (user_input == "0"):
                    print(0)
                    switch = False
                else:
                    
                    print("Invalid input.")
            switch = True


        elif (user_input == "2"):
            while switch:
                print(ui.UI(10, None))
                user_input = input(":")

                if (user_input == "1"):
                    user_input = input("File Name: ")
                    temp_wh = import_warehouse(user_input)
                    if temp_wh != -1:
                        wh = temp_wh
                    else:
                        print("Invalid filename!")
                elif (user_input == "2"):
                    user_input = input("File Name: ")
                    export_warehouse(wh, user_input)
                elif (user_input == "0"):
                    switch = False

            switch = True
        elif (user_input == "3"):
            options = [-1, -1]

            while switch:
                print(ui.UI(12, options))
                user_input = input(":")

                if (user_input == "1"):
                    wh.edit_worker()

                elif (user_input == "2"):
                    wh.edit_arrivals()

                elif (user_input == "3"):
                    wh.edit_shelfs()
                elif (user_input == "4"):
                    wh.edit_items()
                elif (user_input == "5"):
                    wh.edit_time_on_shelf()
                elif (user_input == "0"):
                    switch = False

            switch = True
            
        elif (user_input == "4"):
            options = [-1, -1]

            while switch:
                print(ui.UI(11, options))
                user_input = input(":")

                if (user_input == "1"):
                    inval = input(": ")
                    if inval.isnumeric():
                        options[0] = int(inval)
                    else:
                        print("Value is not a number")

                elif (user_input == "2"):
                    try:
                        user_input = float(input(": "))
                        if not (user_input <= 0):
                            options[1] = float(user_input)
                        else:
                            print("Enter value above 0")
                    except ValueError:
                        print("Value is not a number")

                elif (user_input == "3"):
                    if (-1 in options):
                        print("Invalid settings")
                    else:
                        try:
                            with_scanning = wh.simulate(options[0], options[1], False)
                            without_scanning = wh.simulate(options[0], options[1], True)
                            print(f"Without our solution the item would spend on average: {with_scanning[0]} seconds in the warehouse. And avrage time spent scanning is {with_scanning[1]} seconds")
                            print(f"With our solution the item would spend on average: {without_scanning[0]} seconds in the warehouse. And no scan time")
                            if not (with_scanning[0] == 0):
                                print(f"That's a {(int((1 - without_scanning[0]/with_scanning[0])*100))}% decrease in time!")
                            else:
                                print("No items arrived in departures")
                        except:
                            print("Something went wrong with the simulation, are you sure you entered all values correctly and that items have time to leave the warehouse?")
                    
                elif (user_input == "0"):
                    switch = False

            switch = True

        elif (user_input == "0"):
            print(0)
            switch = False

        else:
            print(ui.UI(0, None))
            print("Invalid input.")



main()
