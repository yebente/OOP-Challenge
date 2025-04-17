class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    # Let each group member add their methods here

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