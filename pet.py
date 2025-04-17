class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    # Let each group member add their methods here

    def eat(self):
     """
     Reduces hunger by 3, but never lets it go below 0.
     increases happiness by 1 but doesn't go beyond 10
     """
     if self.hunger >= 3:
        self.hunger -= 3
     else:
         self.hunger = 0
     self.happiness = min(self.happiness + 1, 10)
     print(f"{self.name} has eaten.")

    def sleep(self):
     """adds energy by 5 but doesn't go beyond 10"""
     self.energy = min(self.energy + 5, 10)
     print(f"{self.name} has slept.")

    def play(self):
        """Decreases energy by 2 and increase happiness by 1"""
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 1, 10)
            self.hunger = min(self.hunger + 1, 10)
            print("You played with your pet.")
        else:
            print(f"{self.name} is too tired to play.")

    #This will be used to print the status as required
    def get_status(self):
        print(f"\n{self.name}'s current status: \nHunger: {self.hunger}\nEnergy: {self.energy}\nHappiness: {self.happiness}\nTricks: {', '.join(self.tricks) if self.tricks else 'None'}")
    
    