#Tamagotchi -Updated
#Burke Sullivan - ITM 360





#Parent class pet

import random
# class attributes
class Pet:
    # class attributes
    cleanliness_max = 10
    food_reduce = 2
    food_max = 10
    food_warning = 3
    boredom_reduce = 2
    boredom_max = 10
    health_max = 10
    sounds = ['Tomagotchi!', 'Grrr...']
# Parent class constructor - paramater for Pet name - added health attribute
    def __init__(self, name):
        self.name = name
        self.hygiene = random.randint(0,self.cleanliness_max)
        self.food = random.randint(0, self.food_max) # random integer between 5 - 10
        self.boredom = random.randint(0, self.boredom_max) # random integer for Pet boredom
        self.health = self.health_max #health setting for pet - added customization
        self.sounds = self.sounds[:]  # Copy of the class attribute - [:] slicing keeps class list memory stored when changed later
# clock tick method -
    def clock_tick(self):
        self.food = max(self.food - self.food_reduce, 0)
        self.boredom = min(self.boredom + 1, self.boredom_max)
        if self.food < self.food_warning or self.boredom > self.boredom_max / 2:
            self.health -= 1
        else:
            self.health = min(self.health + 1, self.health_max)


    # Bath function for pet
    def bathe(self):
        if self.hygiene >= self.cleanliness_max:
            print(f"{self.name} is annoyed by the unnecessary bathe.")
        else:
            self.hygiene = min(self.hygiene + 3, self.cleanliness_max)
            print(f"{self.name} feels refreshed!")
# greet method - pet returns name attribute and sound
    def greet(self):
        print(f"{self.name} says:", random.choice(self.sounds))
        self.reduce_boredom() # call boredom
# feed method
    def feed(self):
        meal = random.randint(self.food, self.food_max)
        self.food = min(self.food + meal, self.food_max)
        print(f"{self.name}'s food level is now at {self.food}/{self.food_max}.")

#Play method
    def play(self):
        print(f"Playing with {self.name}...")
        self.reduce_boredom()
# teach method - added customized
    def teach(self, sound):
        self.sounds.append(sound)
        print(f"{self.name} has learned to say {sound}!")
        self.reduce_boredom() # call boredome level
# Mood method that is set based of boredome level and food level
    def mood(self):
        if self.food >= self.food_warning and self.boredom <= self.boredom_max / 2:
            return "happy"
        elif self.food < self.food_warning:
            return "hungry"
        else:
            return "bored"
# reduce boredom
    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - 3)
# string function to print status for pet class
    def status(self):
        print(f"{self.name}'s status:\nFood: {self.food}/{self.food_max}\nBoredom: {self.boredom}/{self.boredom_max}\nHealth: {self.health}/{self.health_max}\nMood: {self.mood()}")

#child class for dinosaur pet - customizable features for mood - health and die functions
class Dino(Pet):
    # added dinosuar size for overall size
    Size = 100
    sounds = ["rawr"]

    def mood(self):
        if self.food >= self.food_warning and 3 <= self.boredom <= 5:
            return "playful"
        elif self.boredom < 3:
            return "sleepy"
        elif self.boredom > 5:
            return "irritated"
        else:
            return "randomly annoyed" if random.randint(0, 1) == 0 else "curious"
    # Added method to increase size of DINO
    def inc_size(self, increase=10):  # Default increase amount set to 10
        self.Size += increase  # Increase the size attribute by the specified amount
        print(f"{self.name} has grown! Current size: {self.Size} feet")

    # Override the feed method to include size increase
    # call from parent class feed method
    def feed(self):
        super().feed()  # Call the parent class feed method
        self.inc_size()  # Call the inc_size method to increase the size and print the new size
    #Sub class for cat
class Cat(Pet):
    sounds = ["Meow"]
    #Tom and jerry function
    def chase_rat(self, rat=False):
        if rat:
            print(f"{self.name} is chasing a rat!")
    #Mood for cats - method (same method in all classes)
    def mood(self):
        if self.boredom < 3:
            return "feeling grumpy"
        elif self.boredom > 5:  # really bored if reached above 5
            return "absolutely bored!"
        else:
            return "randomly annoyed" if random.randint(0, 1) == 0 else "curious"


# main function with all instances enabled based of users choice of pet
def main():
    pet_name = input("What is your pet's name? ")
    pet_type = input("What type of pet do you want (dino, cat, or other)? ").lower()

    if pet_type == "dino":
        pet = Dino(pet_name)
    #calling cat method
    elif pet_type == "cat":
        pet = Cat(pet_name)
        pet.chase_rat(True)
    else:
        pet = Pet(pet_name)

    # Adjusted interaction loop to include bathing and handle new pet types
    while True:
        action = input("What would you like to do (feed/play/teach/greet/status/bathe/quit)? ").lower()

        if action in ["feed", "play", "teach"]:
            pet.clock_tick()

        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "teach":
            sound = input(f"What sound do you want to teach {pet_name}? ")
            pet.teach(sound)
        elif action == "greet":
            pet.greet()
        elif action == "bathe":
            pet.bathe()
        elif action == "status":
            pet.status()
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please choose again.")

        if pet.health <= 0:
            print(f"{pet_name} has passed away... :(")
            break

# if name == main - used to call program
if __name__ == "__main__":
    main()



