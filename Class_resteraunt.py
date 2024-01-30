##In class Resteraunt

class Restaurant:

    def __init__(self, name, cuisine, deals=0):
        self.name = name
        self.cuisine = cuisine
        self.deals = deals  # Initialize deals with a default value of 0

    def describe_restaurant(self):  # Method names should be lowercase with underscores as per PEP 8
        print(f'This restaurant is called {self.name}.')
        print(f'It serves {self.cuisine} cuisine.')

    def open_restaurant(self):
        print(f'The {self.name} is now open - serving {self.cuisine} cuisine.')

    def set_deals(self, value):
        self.deals = value
        print(f'There is a {value}% off deal today!')

def instance_one():
    my_place = Restaurant("Haiku", "Japanese", 50)  # Corrected spelling and adjusted parameter order
    print(f"Have you heard about {my_place.name}?")
    print(f"They have an amazing {my_place.cuisine} menu.")
    if my_place.deals:  # Check if there are any deals
        print(f"They are currently offering a {my_place.deals}% off deal!")

instance_one()

def instance_two():
    fav_place = Restaurant("Bob's Burgers", "American")  # Removed the deals parameter, assuming no deal by default
    fav_place.set_deals(50)  # Set the deals using the 'set_deals' method
    print(f"Have you heard about {fav_place.name}?")
    print(f"They have an amazing {fav_place.cuisine} menu.")
    if fav_place.deals:
        print(f"They are currently offering a {fav_place.deals}% off deal!")

instance_two()

def instance_three():
    now_open = Restaurant("Taco bell", "mexican")
    now_open.describe_restaurant()
    now_open.open_restaurant()


instance_three()




