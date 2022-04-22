import itertools
from re import T
import re

import simpy
from source.item import *
from source.shelf import *
from source.worker import *
from source.risk import *
from source.Store import *
from source.UI import *
import random


class warehouse:
    def __init__(self):
        self.shelves = []           #An array with the warehouses shelves
        self.arrivals = None        #The arrivals terminal, is a shelf
        self.departures = None      #The departures terminal, is a shelf
        self.workers = []           #An array of the warehouses workers
                                    #the nuber of simulated ticks in a second,
                                    #a higer value increases the precision of the simulation.
        self.avg_shelfed = 10

        self.cur_time = 0           #The current time in the warehouse in seconds
        self.global_risks = []      #A list of the global risks that can occur
        self.item_risks = []        #Specific constant item risks like size or handeling limitations

        self.env = None
        self.progress = 10


    def edit_worker(self):
        ui = UI()
        index = 1
        for worker in self.workers:
            print(f"{index}. Worker {index}: Scan time: {worker.scan_time}, Walking Speed: {worker.speed}, Item handeling time: {worker.scan_time}")
            index += 1
        index = input("Worker to Edit: ")
        while not index.isnumeric():
            print("Enter a valid number or enter 0 to exit")
            index = input("Worker to Edit: ")
        index = int(index)
        if index <= 0 or index > len(self.workers):
            return
        worker = self.workers[index - 1]
        while True:
            print(ui.UI(13, [worker.scan_time, worker.speed, worker.scan_time]))
            user_input =  input(": ")
            if (user_input == "1"):
                user_input = input("Scan time: ")
                if user_input.isnumeric():
                    worker.scan_time = int(user_input)
                else:
                    print("Invalid")
            elif (user_input == "2"):
                user_input = input("Walking Speed: ")
                if user_input.isnumeric():
                    worker.speed = int(user_input)
                else:
                    print("Invalid")
            elif (user_input == "3"):
                user_input = input("Item handeling time: ")
                if user_input.isnumeric():
                    worker.scan_time = int(user_input)
                else:
                    print("Invalid")
            elif (user_input == "4"):
                self.workers.pop(index)
                return
            elif (user_input == "0"):
                return
            else:
                print("Invalid")


    def edit_arrivals(self):
        while True:
            print(f"1. EditArrivals capacity: {self.arrivals.store.capacity}")
            print("0. Back")
            user_input =  input(": ")
            if (user_input == "1"):
                user_input = input("Capacity: ")
                if user_input.isnumeric():
                    self.arrivals.store = Store(int(user_input))
                else:
                    print("Invalid")
            elif (user_input == "0"):
                return
            else:
                print("Invalid")


    def edit_shelfs(self):
        ui = UI()
        index = 1
        for shelf in self.shelves:
            print(f"{index}. Shelf {index}: Shelf capacity: {shelf.store.capacity}, Distance from arrivals: {shelf.distance_from_arrivals}, Distance from departures: {shelf.distance_from_departure}")
            index += 1

        index = input("Shelf to Edit: ")
        while not index.isnumeric():
            print("Enter a valid number or enter 0 to exit")
            index = input("Shelf to Edit: ")
        index = int(index)
        if index <= 0 or index > len(self.shelves):
            return
        shelf = self.shelves[index - 1]
        while True:
            print(ui.UI(14, [shelf.store.capacity, shelf.distance_from_arrivals, shelf.distance_from_departure]))
            user_input =  input(": ")
            if (user_input == "1"):
                user_input = input("Capacity: ")
                if user_input.isnumeric():
                    shelf.store = Store(int(user_input))
                else:
                    print("Invalid")
            elif (user_input == "2"):
                user_input = input("Distance from arrivals: ")
                if user_input.isnumeric():
                    shelf.distance_from_arrivals = int(user_input)
            elif (user_input == "3"):
                user_input = input("Distance from departures: ")
                if user_input.isnumeric():
                    shelf.distance_from_departure = int(user_input)
            elif (user_input == "4"):
                self.shelves.pop(index)
                return
            elif (user_input == "0"):
                return
            else:
                print("Invalid")

    def edit_items(self):
        ui = UI()
        index = 1
        for risk in self.item_risks:
            print(f"{index}. Risk: {risk.name}, Probability (1-100%): {risk.probability}, Time penalty: {risk.magnitude}, Risk Type: {risk.type}")
            index += 1
        index = input("Risk to Edit: ")
        while not index.isnumeric():
            print("Enter a valid number or enter 0 to exit")
            index = input("Risk to Edit: ")
        index = int(index)
        if index <= 0 or index > len(self.item_risks):
            return
        risk = self.item_risks[index - 1]
        while True:
            print(ui.UI(15, [risk.name, risk.probability, risk.magnitude]))
            user_input =  input(": ")
            if (user_input == "1"):
                risk.name = input("Name: ")
            elif (user_input == "2"):
                user_input = input("Probability: ")
                if user_input.isnumeric():
                    risk.probability = int(user_input) / 100
                else:
                    print("Invalid")
            elif (user_input == "3"):
                user_input = input("Time penalty: ")
                if user_input.isnumeric():
                    risk.magnitude = int(user_input)
                else:
                    print("Invalid")
            elif (user_input == "4"):
                self.item_risks.pop(index)
            elif (user_input == "0"):
                return
            else:
                print("Invalid")
    

    def edit_time_on_shelf(self):
        while True:
            print(f"1. Average item time on shelves: {self.avg_shelfed} seconds")
            print("0. Back")
            user_input =  input(": ")
            if (user_input == "1"):
                user_input = input("Average item time on shelves: ")
                if user_input.isnumeric():
                    self.avg_shelfed = int(user_input)
                else:
                    print("Invalid")
            elif (user_input == "0"):
                return
            else:
                print("Invalid")

    def edit_time_on_shelf_mock(self, u_inputs):
        while True:
            print(f"1. Average item time on shelves: {self.avg_shelfed} seconds")
            print("0. Back")
            user_input =  u_inputs.pop(0)
            if (user_input == "1"):
                user_input = u_inputs.pop(0)
                if user_input.isnumeric():
                    self.avg_shelfed = int(user_input)
                else:
                    print("Invalid")
            elif (user_input == "0"):
                return
            else:
                print("Invalid")

    def create_worker_lst(self, amount, scan_time, speed, item_handeling_time):
        """Create one or multiple workers and add them to the warehouse"""
        for i in range(amount):
            self.workers.append(worker(scan_time, speed, item_handeling_time, i, Store(1)))


    def create_item(self, testing=False):
        """Returns an item with the avalible risks"""
        temp_risk = []

        for irisk in self.item_risks:
            if irisk.type == "handeling":
                if random.uniform(0,1) < irisk.probability: #Gives the item constant risk like size or fragile
                    temp_risk.append(irisk)                 #NOTE This does nothing at the moment, only scanning risks are implemented
            else:
                temp_risk.append(irisk)

        final_risk_lst = []

        for i in temp_risk:
            final_risk_lst.append(risk(i.name, i.type, i.probability, i.magnitude))
        if testing: # Dummy code for testing purposes outside of the simpy environment
            return item(final_risk_lst, 0)
        return item(final_risk_lst, self.env.now)


    def create_shelf(self, capacity, distance_from_arrivals, distance_from_departure):
        """Creates a shelf and appends it to the warehouse"""
        self.shelves.append(shelf(len(self.shelves), Store(capacity), distance_from_arrivals, distance_from_departure))


    def create_arrivals(self, capacity):
        """Creates arrivals"""
        self.arrivals = shelf(0, Store(capacity))


    def create_departures(self):
        """Creates departures"""
        self.departures = shelf(0, Store(-1))


    def gen_items(self, frequency):
        """Generates items into arrivals"""
        while True:
            yield self.env.timeout(frequency)
            itm = self.create_item()
            self.arrivals.store.put(itm)    #Puts the generated item into arrivals

    def get_progress(self, sim_time):
        """Prints the progress of the simulation"""
        while True:
            yield self.env.timeout(1)

            time = self.env.now / sim_time * 100

            if self.progress < time:
                print(f"Progress: {int(time)}%")
                self.progress += 10


    def run(self, no_scanning):
        """The main function to contoll the simulation"""
        while True:
            free_workers = []
            for w in self.workers:          #Find all workers with no task
                if w.is_waiting():
                    free_workers.append(w)

            free_shelves = []               #Find all full shelves
            for s in self.shelves:
                if not s.is_full():
                    free_shelves.append(s)

            if free_workers:                    #Give the free workers a job
                if random.randint(1, 2) == 1:   #Randomize if the worker should move items from arrivals or shevles 
                    for shlf in self.shelves:   #Find a shelf with item that should be moved and move it
                        chosen_one = random.choice(free_workers)
                        itm = shlf.item_to_be_moved(self.env, chosen_one)
                        if itm:
                            chosen_one.move(self.env, shlf.distance_from_arrivals + shlf.distance_from_departure, self.departures, itm, no_scanning)
                            itm.exited = self.env.now + chosen_one.time_for_item(itm, shlf.distance_from_arrivals + shlf.distance_from_departure, no_scanning) + self.avg_shelfed
                            break

                elif not self.arrivals.is_empty() and free_shelves:
                    chosen_one = random.choice(free_workers)    #Move an item from arrivals to a shelf
                    chosen_shelf = random.choice(free_shelves)
                    itm = self.arrivals.store.get()
                    chosen_one.move(self.env, chosen_shelf.distance_from_arrivals, chosen_shelf, itm, no_scanning)
                    itm.when_to_move += self.avg_shelfed + self.env.now

            yield self.env.timeout(0.1)

    def run_mock(self, no_scanning, rand, expected):
        # """TEST: The main function to contoll the simulation"""
        result = ""

        while True:
            result += "A"
            free_workers = []
            result += "-B"
            for w in self.workers:          #Find all workers with no task
                result += "-C"
                if w.is_waiting():
                    result += "-D"
                    free_workers.append(w)
                    result += "-E"
                result += "-F"

            result += "-G"
            free_shelves = []               #Find all full shelves
            result += "-H"

            for s in self.shelves:
                result += "-I"
                if not s.is_full():
                    result += "-J"
                    free_shelves.append(s)
                    result += "-K"
                result += "-L"

            result += "-M"

            if free_workers:                    #Give the free workers a job
                result += "-N"
                if rand == 1:   #Randomize if the worker should move items from arrivals or shevles
                    result += "-O"
                    for shlf in self.shelves:   #Find a shelf with item that should be moved and move it
                        result += "-P"
                        chosen_one = random.choice(free_workers)
                        itm = shlf.item_to_be_moved(self.env, chosen_one)
                        result += "-Q"
                        if itm:
                            result += "-S"
                            chosen_one.move(self.env, shlf.distance_from_arrivals + shlf.distance_from_departure, self.departures, itm, no_scanning)
                            itm.exited = self.env.now + chosen_one.time_for_item(itm, shlf.distance_from_arrivals + shlf.distance_from_departure, no_scanning) + self.avg_shelfed
                            result += "-T"
                            break
                        result += "-R"
                    result += "-U"

                elif not self.arrivals.is_empty() and free_shelves:
                    result += "-V"
                    result += "-W"
                    chosen_one = random.choice(free_workers)    #Move an item from arrivals to a shelf
                    chosen_shelf = random.choice(free_shelves)
                    itm = self.arrivals.store.get()
                    chosen_one.move(self.env, chosen_shelf.distance_from_arrivals, chosen_shelf, itm, no_scanning)
                    itm.when_to_move += self.avg_shelfed + self.env.now
                    result += "-X"
                else:
                    result += "-V"
                    result += "-Y"
            else:
                result += "-Z"

            if(all(x in result.split("-") for x in expected.split("-"))): 
                print("\033[1;32m Success \033[0m")
            else: 
                print("\033[1;31m Failed \033[0m")
                print(f"   unexpected: \n   {result} \n   {expected}")

            yield self.env.timeout(10)


    def simulate(self, sim_time, arrivals_freq, no_scanning):
        """Simulates sim_time number of seconds with items arraving and departing based on arrivals_freq"""
        self.progress = 10          #Resets the progressbar
        
        for shlf in self.shelves:   #Resets the contents of all shelves
            shlf.store.empty()

        self.arrivals.store.empty()     #Resets arrivals
        self.departures.store.empty()   #Resets departures

        tempw = self.workers[:]         #Due to simpy weirdness the workers must be recreated to reset them
        self.workers = []
        for w in tempw:
            self.create_worker_lst(1, w.scan_time, w.speed, w.item_handeling_time)

        for wor in self.workers:        #Reset worker inventory
            wor.inventory.empty()       

        self.env = simpy.Environment()                      #Create simulation environment
        self.env.process(self.gen_items(arrivals_freq))     #Make gen_items a process
        self.env.process(self.run(no_scanning))             #Make run a process
        self.env.process(self.get_progress(sim_time))       #Make get_progress a process 

        self.env.run(until=sim_time)                        #Run the simulation

        ret_val = 0
        avr_time_scanning = 0

        tot_time_items = 0
        for itm in self.departures.store.items:             #Create the return values
            tot_time_items += itm.exited - itm.enterd
        if not (len(self.departures.store.items) == 0):
            ret_val = tot_time_items/len(self.departures.store.items)

        avr_time_scanning = 0
        for worker in self.workers:
            avr_time_scanning = worker.time_spent_scanning
        if not (len(self.workers) == 0):
            avr_time_scanning = avr_time_scanning / len(self.workers)

        return [ret_val, avr_time_scanning]

    def simulate_mock(self, arrivals_freq, no_scanning, rand, expected):
        """Simulates sim_time number of seconds with items arraving and departing based on arrivals_freq"""
        self.progress = 10          #Resets the progressbar
        
        # for shlf in self.shelves:   #Resets the contents of all shelves
        #     shlf.store.empty()

        # self.arrivals.store.empty()     #Resets arrivals
        # self.departures.store.empty()   #Resets departures

        tempw = self.workers[:]         #Due to simpy weirdness the workers must be recreated to reset them
        self.workers = []
        for w in tempw:
            self.create_worker_lst(1, w.scan_time, w.speed, w.item_handeling_time)

        # for wor in self.workers:        #Reset worker inventory
        #     wor.inventory.empty()       

        self.env = simpy.Environment()                      #Create simulation environment
        self.env.process(self.gen_items(arrivals_freq))     #Make gen_items a process
        self.env.process(self.run_mock(no_scanning, rand, expected))             #Make run a process

        self.env.run(until=1)                         #Run the simulation

        ret_val = 0
        avr_time_scanning = 0

        tot_time_items = 0
        for itm in self.departures.store.items:             #Create the return values
            tot_time_items += itm.exited - itm.enterd
        if not (len(self.departures.store.items) == 0):
            ret_val = tot_time_items/len(self.departures.store.items)

        avr_time_scanning = 0
        for worker in self.workers:
            avr_time_scanning = worker.time_spent_scanning
        if not (len(self.workers) == 0):
            avr_time_scanning = avr_time_scanning / len(self.workers)

        return [ret_val, avr_time_scanning]

