class risk:
    def __init__(self, name, itype, probability, magnitude):
        self.name = name                        #String of risk name
        self.type = itype                       #String of risk type. can be: scanning, moving or handeling
        self.probability = probability/100      #Float of risk probability in constant risks the is used as the percentage of items with this risk
        self.magnitude = magnitude              #Time penalty in seconds