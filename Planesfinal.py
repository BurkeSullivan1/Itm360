#Planes final Program
#Burke Sullivan
#Sources: Chat GPT
import csv


# Create Classes: Passenger and Planes
# Passenger - name and food preference attributes

class Passenger:
    def __init__(self, name="empty", food_preference="none"):
        self.__name = name
        self.__food_preference = food_preference

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def food_preference(self):
        return self.__food_preference

    @food_preference.setter
    def food_preference(self, value):
        if value.lower() in ["chicken", "pasta", "special"]:
            self.__food_preference = value.lower()
        else:
            self.__food_preference = "none"

    def __str__(self):
        return f"{self.__name} ({self.__food_preference})"

#check instances for class passenger - needed str function - will be used in passenger class

class Plane:
    def __init__(self, plane_id, max_seats, has_meal=False):
        self.plane_id = plane_id
        self.__has_meal = has_meal
        self.__num_on_plane = 0
        self.__max_seats = max_seats
        self.__bookings = [[Passenger() for _ in range(4)] for _ in range(max_seats // 4)]
    # Getters and Setters
    @property
    def has_meal(self):
        return self.__has_meal

    @property
    def num_on_plane(self):
        return self.__num_on_plane

    @property
    def max_seats(self):
        return self.__max_seats

    @property
    def bookings(self):
        return self.__bookings

    # Setters
    @has_meal.setter
    def has_meal(self, value):
        self.__has_meal = value

    @bookings.setter
    def bookings(self, value):
        self.__bookings = value

    # Add passenger method

    # checks if there is a 'seat' based off "empty"

    #Returns passenger and adds counter to number of people to plane

    def add_passenger(self, passenger, row, seat):
        if not self.__bookings[row-1][seat-1].name == "empty":
            print("Seat is already booked.")
            return
        self.__bookings[row-1][seat-1] = passenger
        self.__num_on_plane += 1
        if not self.__has_meal:
            passenger.food_preference = "snack"
# displaying seating
# source: ChatGPT - asked to read from csv file and display seat ordination
    def display_seating(self):
        for row in self.__bookings:
            print(' | '.join(str(passenger) if passenger.name != "empty" else "Empty seat" for passenger in row))
# Method to check if plane seats if full
    def is_plane_full(self):
        return self.__num_on_plane >= self.__max_seats
# Method to count food pref on plane
# Dictionary method - starting at 0
# iterate through seats on plane - checks food preference and adds one to food counter
    def count_food_preferences(self):
        food_counts = {"chicken": 0, "pasta": 0, "special": 0, "snack": 0, "none": 0}
        for row in self.__bookings:
            for seat in row:
                if seat.name != "empty":
                    food_counts[seat.food_preference] += 1
        return food_counts
# Whos on the plane method and in which seat
# Creates passengers list and iterates through bookings array
    def alphabetical_list_of_passengers(self):
        passenger_list = []
        for row in self.__bookings:
            for seat in row:
                if seat.name != "empty":
                    passenger_list.append((seat.name, seat.food_preference))
        passenger_list.sort()
        return passenger_list
# Method to find passenger on plane and returns the seat
# Source Chatgpt: "Help me find passenger in bookings csv"
# Paramater from inputted passenger name
    def find_passenger_seat(self, passenger_name):
        # For loop -enumerate gets the index of the row and the row itself
        for i, row in enumerate(self.__bookings):
            for j, seat in enumerate(row):
                #is that passenger on the plane given passenger_name paramater
                if seat.name == passenger_name:
                    # returns tuple below - i is row index and j is seat index
                    return i+1, j+1  # Adjusting for human-readable indexing
        return None # else if passenger is not on plane
# Method to check available seats on plane that are empty
    def list_available_seats(self):
        available_seats = []
        for i, row in enumerate(self.__bookings):
            for j, seat in enumerate(row):
                if seat.name == "empty":
                    available_seats.append((i+1, j+1))  # Adjusting for human-readable indexing
        return available_seats
#checks if seats are booked based of 2d array list
#indexing starts at 0 so subtract 1 (python lists are zero indexed)
    def check_seat_booked(self, row, seat):
        return self.__bookings[row-1][seat-1].name != "empty"


#method checks if number of people on plane is = or greater than number of total seats
    def is_plane_full(self):
        return self.num_on_plane >= self.max_seats


######################################


def read_planes(filename):
    planes = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header line if your TXT file has one
        for line in file:
            plane_id, _, _, _, rows, num_per_row = line.strip().split(',')
            max_seats = int(rows) * int(num_per_row)
            has_meal = True  # Assuming all planes have meals, adjust based on your data
            planes.append(Plane(plane_id, max_seats, has_meal))
    return planes

def get_plane_seating_from_csv(planes, filename='bookings.csv'):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            plane_id = row['Plane']
            # Find the corresponding plane object
            plane = next((p for p in planes if p.plane_id == plane_id), None)
            if plane:
                passenger = Passenger(row['Name'], row['Meal'])
                row_number = int(row['Row'])
                seat_number = int(row['Seat'])
                if row_number <= (plane.max_seats // 4) and seat_number <= 4:
                    plane.add_passenger(passenger, row_number, seat_number)

def main_menu():
    print("1. Add Passenger")
    print("2. List Planes")
    print("3. List Passengers")
    print("4. Food Count")
    print("5. Find Passenger")
    print("6. End Program")
    return input("Choose an option: ")

def add_passenger(planes):
    plane_id = input("Enter the plane ID: ")
    name = input("Enter passenger name: ")
    food_preference = input("Enter food preference (chicken, pasta, special, or none): ")
    row = int(input("Enter row number: "))
    seat = int(input("Enter seat number: "))

    # Find the plane
    # Efficent way to search through planes list whose plane_id attribute matches the given plane_id- assigns Plane object to variable plane
    plane = next((p for p in planes if p.plane_id == plane_id), None)
    if plane:
        if not plane.is_plane_full():
            if plane.check_seat_booked(row, seat):
                print("This seat is already booked. Please choose a different seat.")
            else:
                passenger = Passenger(name, food_preference)
                plane.add_passenger(passenger, row, seat)
                print(f"Passenger {name} added successfully.")
        else:
            print("The plane is full. Cannot add more passengers.")
    else:
        print("Plane not found.")


def list_planes(planes):
    for plane in planes:
        print(f"Plane ID: {plane.plane_id}, Seats Taken: {plane.num_on_plane}/{plane.max_seats}, Meal: {'Yes' if plane.has_meal else 'No'}")

def list_passengers(planes):
    plane_id = input("Enter the plane ID to list passengers: ")
    plane = next((p for p in planes if p.plane_id == plane_id), None)
    if plane:
        passengers = plane.alphabetical_list_of_passengers()
        if passengers:
            for name, food_preference in passengers:
                print(f"Name: {name}, Food Preference: {food_preference}")
        else:
            print("No passengers on this plane.")
    else:
        print("Plane not found.")


def food_count(planes):
    plane_id = input("Enter the plane ID to count food preferences: ")
    plane = next((p for p in planes if p.plane_id == plane_id), None)
    if plane:
        food_counts = plane.count_food_preferences()
        for food, count in food_counts.items():
            print(f"{food.title()}: {count}")
    else:
        print("Plane not found.")


def find_passenger(planes):
    name = input("Enter the name of the passenger to find: ")
    for plane in planes:
        seat = plane.find_passenger_seat(name)
        if seat:
            print(f"{name} is in seat {seat[0]}, {seat[1]} on plane {plane.plane_id}.")
            break
    else:
        print(f"Passenger {name} not found on any plane.")

def main():
    planes = read_planes("planes.txt")  # Initialize planes from TXT file
    get_plane_seating_from_csv(planes, "bookings.csv")  # Update planes with bookings from CSV file

    # Your existing menu and user interaction logic follows here
    while True:
        choice = main_menu()
        # Process user choice

        if choice == '1':
            add_passenger(planes)
        elif choice == '2':
            list_planes(planes)
        elif choice == '3':
            list_passengers(planes)
        elif choice == '4':
            food_count(planes)
        elif choice == '5':
            find_passenger(planes)
        elif choice == '6':
            print("Ending program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
