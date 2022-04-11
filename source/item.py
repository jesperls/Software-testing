class item:
    def __init__(self, risks, enterd):
        self.risks = risks      #An array of risks that can occur to the item
        self.enterd = enterd    #The time the item enterd the warehouse
        self.exited = -1        #The time the item exited the warehouse
        self.when_to_move = -1
