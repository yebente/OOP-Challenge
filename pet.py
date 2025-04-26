import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"🍖 {self.name} is munching happily!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"😴 {self.name} is dozing off into dreamland...")

    def play(self):
        if self.energy <= 0:
            print(f"⚡ {self.name} is too tired to play. Let them rest!")
            return
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"🐾 {self.name} is playing joyfully!")

    def get_status(self):
        # Randomized mood generator
        moods = ["happy 😸", "sleepy 😴", "bored 😐", "excited 🤩"]
        mood = random.choice(moods)
        
        print(f"\n📋 {self.name}'s Current Status:")
        print(f"   🥘 Hunger: {self.hunger}/10")
        print(f"   ⚡ Energy: {self.energy}/10")
        print(f"   😸 Happiness: {self.happiness}/10")
        print(f"   🧠 Mood: {mood}")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"🎓 {self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"\n🏆 {self.name}'s Trick List:")
            for trick in self.tricks:
                print(f"   ➡️ {trick}")
        else:
            print(f"😕 {self.name} hasn't learned any tricks yet.")
