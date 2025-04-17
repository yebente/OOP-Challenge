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
        # The current status of the pet
        print(f"\n{self.name}'s status:")
        print(f"Hunger: [{'|' * self.hunger}{' ' * (10 - self.hunger)}] {self.hunger}/10")
        print(f"Energy: [{'|' * self.energy}{' ' * (10 - self.energy)}] {self.energy}/10")
        print(f"Happiness: [{'|' * self.happiness}{' ' * (10 - self.happiness)}] {self.happiness}/10")
        
        if self.hunger >= 8:
            print("WARNING: I am Starving!")
        if self.energy <= 2:
            print("WARNING: I am too tired to play!")
        if self.happiness <= 2:
            print("WARNING: I am sad!")

    def train(self, trick):
        # Teach the pet a new trick
        if not hasattr(self, 'tricks'):
            self.tricks = []
        if trick in self.tricks:
            print(f"{self.name} already knows '{trick}'.")
        else:
            self.tricks.append(trick)
            print(f"Successfully taught {self.name} the trick '{trick}'!")
            self.happiness = min(10, self.happiness + 1)

    def show_tricks(self):
        # Show the pet's tricks
        if not hasattr(self, 'tricks') or not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"\n{self.name}'s tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")





    def __str__(self):
        return f"{self.name} is an amazing pet."