import random

class worker:
    def __init__(self, scan_time, speed, item_handeling_time, id, inventory):
        self._is_waiting = True            #True if the worker is wating for work

        self.scan_time = scan_time         #The number of seconds it takes to scan a given item
        self.speed = speed                 #The speed if the worker in m/s

        self.item_handeling_time = item_handeling_time         #The time it takes to handel an item in seconds

        self.id = id

        self.inventory = inventory         #The workers inventory to contain items 

        self.time_spent_scanning = 0       #Total time spent scanning

    def is_wating(self):
        """Returns True if the worker is waiting for work"""
        return self._is_waiting

    def time_for_item(self, itm, distance, no_scanning):
        """Returns the time it takes to deliver an item"""
        time = distance / self.speed + self.item_handeling_time + self.scan_time
        self.time_spent_scanning += self.scan_time

        if no_scanning:
            time -= self.scan_time
            self.time_spent_scanning -= self.scan_time

        for risk in itm.risks:
            if (risk.type == "handeling"):
                time += risk.magnitude

            elif not (no_scanning and risk.type == "scanning"):
                if (random.uniform(0,1) < risk.probability):
                    time += risk.magnitude
                    self.time_spent_scanning -= self.scan_time

            elif (risk.type == "moving"):
                if (random.uniform(0,1) < risk.probability):
                    time += risk.magnitude

        return time

    def move_process(self, env, distance, target, itm, no_scanning):
        """Gives the worker a task and timesout the worker"""
        self.start = env.now
        #print(f"{self.id} Started at {self.start}")
        self._is_waiting = False
        self.inventory.put(itm)
        # print(f"{env.now}")
        time = self.time_for_item(itm, distance, no_scanning)
        itm.when_to_move = time
        yield env.timeout(time)
        # print(f"{env.now}")
        target.store.put(self.inventory.get())
        self._is_waiting = True
        #print(f"{self.id} Finished at {env.now}")

    def move(self, env, distance, target, itm, no_scanning):
        """Creates the move process"""
        env.process(self.move_process(env, distance, target, itm, no_scanning))

    def place_down(self, env):
        """Returns the item in the workers inventory"""
        return self.inventory.get()

    def is_waiting(self):
        """Returns True if the worker is wating for work"""
        return self._is_waiting
