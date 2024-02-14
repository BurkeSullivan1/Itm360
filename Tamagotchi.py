#Tamagotchi
#Burke Sullivan - ITM 360
#parent class pet

import random
# class attributes
class Pet:
    food_reduce = 2
    food_warning = 5
    boredom_max = 10
    food_max = 10
    health_max = 10
    sounds = ["Hmmmmmm...ahhh"]
# Parent class constructor - paramater for Pet name - added health attribute
    def __init__(self, name):
        self.name = name
        self.food = random.randint(5, self.food_max) # random integer between 5 - 10
        self.boredom = random.randint(0, self.boredom_max) # random integer for Pet boredom
        self.health = self.health_max #health setting for pet - added customization
        self.sounds = self.sounds[:]  # Copy of the class attribute - [:] slicing keeps class list memory stored when changed later
# clock tick method -
    def clock_tick(self):
        self.food -= self.food_reduce
        self.boredom += 1
        if self.food < self.food_warning or self.boredom > self.boredom_max / 2:
            self.health -= 1
        else:
            self.health = min(self.health + 1, self.health_max)
# greet method - pet returns name attribute and sound
    def greet(self):
        print(f"{self.name} says:", random.choice(self.sounds))
        self.reduce_boredom()
# feed method
    def feed(self):
        if self.food >= self.food_max:
            print(f"{self.name} is not hungry.")
        else:
            self.food = min(self.food + 3, self.food_max)  # Ensure food does not exceed max
            food_percentage = (self.food / self.food_max) * 100  # Calculate the percentage
            print(f"{self.name}'s food level is now at {food_percentage:.0f}% full.")


    def play(self):
        print(f"Playing with {self.name}...")
        self.reduce_boredom()
# teach method - added customized
    def teach(self, sound):
        self.sounds.append(sound)
        print(f"{self.name} has learned to say {sound}!")
# Mood method that is set based of boredome level and food level
    def mood(self):
        if self.food >= self.food_warning and self.boredom <= self.boredom_max / 2:
            return "happy"
        elif self.food < self.food_warning:
            return "hungry"
        else:
            return "bored"

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - 3)
# string function to print status for pet class
    def status(self):
        print(f"{self.name}'s status:\nFood: {self.food}/{self.food_max}\nBoredom: {self.boredom}/{self.boredom_max}\nHealth: {self.health}/{self.health_max}\nMood: {self.mood()}")

#child class for dinosaur pet - customizable features for mood - health and die functions
class Dino(Pet):
    sounds = ["rawr"]
# mood function - and makes sure both are correct to be returned - is false checks other moods
    def mood(self):
        if self.food >= self.food_warning and 3 <= self.boredom <= 5:
            return "playful"
        elif self.boredom < 3:
            return "sleepy"
        elif self.boredom > 5:
            return "irritated"
        else:
            return "randomly annoyed" if random.randint(0, 1) == 0 else "curious"
#main function - running instances
def main():
    pet_name = input("What is your pet's name? ")
    pet_type = input("What type of pet do you want (dino or cat?)? ").lower()
    if pet_type == "dino":
        pet = Dino(pet_name)
    else:
        pet = Pet(pet_name)

    while True:
        action = input("What would you like to do (feed/play/teach/greet/status/quit)? ").lower()
#Action menu for user - status bar is unchanged when called
        if action in ["feed", "play", "teach"]:
            pet.clock_tick()  # Time progresses only for these actions

        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "teach":
            sound = input(f"What sound do you want to teach {pet_name}? ")
            pet.teach(sound)
        elif action == "greet":
            pet.greet()  # Assuming 'greet' does not advance time
        elif action == "status":
            pet.status()  # Just show the status, no time advancement
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please choose again.")
#function for pet to die
        if pet.health <= 0:
            print(f"{pet_name} has passed away... :(")
            break

if __name__ == "__main__":
    main()

# if name == main - used to call program
if __name__ == "__main__":
    main()



