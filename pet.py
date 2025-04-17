class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
    # Let each group member add their methods here


    #This will be used to print the status as required
    def get_status(self):
        # TODO
        pass
        
    def __str__(self):
        return f"{self.name} is an amazing pet."