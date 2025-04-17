class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    # Let each group member add their methods here
    #Reduces hunger by 3, but never lets it go below 0.
    #increases happiness by 1 but doesn't go beyond 10
    def eat(self):
     if self.hunger >= 3:
        self.hunger -= 3
     else:
         self.hunger = 0
     self.happiness = min(self.happiness + 1, 10)
     print(f"{self.name} has eaten. Hunger is now {self.hunger}, Happiness is {self.happiness}.")
    #adds energy by 5 but doesn't go beyond 10
    def sleep(self):
     self.energy = min(self.energy + 5, 10)
     print(f"{self.name} has slept. Energy is now {self.energy}.")



    def play(self):
        # Decrease energy and increase happiness
        if self.energy > 0:
            self.energy -= 2
            self.happiness += 1
            self.hunger += 1
            print("You played with your pet.")
        else:
            print(f"{self.name} is too tired to play.")
        
        

    #This will be used to print the status as required
    def get_status(self):
        return f"{self.name} is an amazing pet."