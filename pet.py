class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} just ate! Yummy 😋🍗")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} is sleeping... 😴🛏️")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} had fun playing! 🎾😸")
        else:
            print(f"{self.name} is too tired to play. Let them sleep. 💤😿")

    def get_status(self):
        print(f"{self.name}'s Status 📊:")
        print(f"   Hunger: {self.hunger}/10 🍽️")
        print(f"   Energy: {self.energy}/10 ⚡")
        print(f"   Happiness: {self.happiness}/10 😊")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} learned a new trick: {trick} 🎉🧠")

    def show_tricks(self):
        print(f"{self.name} knows these tricks: {', '.join(self.tricks) if self.tricks else 'None yet!'} 🐾✨")
