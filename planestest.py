import csv

# Define the Passenger and PlaneTracker classes
class Passenger:
    def __init__(self, name, meal_preference):
        self.name = name
        self.meal_preference = meal_preference

    def __str__(self):
        return f"{self.name} ({self.meal_preference})"

class PlaneTracker:
    def __init__(self, plane_id):
        self.plane_id = plane_id
        self.seats = [[None for _ in range(4)] for _ in range(32)]  # 32 rows by 4 columns

    def add_passenger(self, passenger, row, seat):
        self.seats[row-1][seat-1] = passenger  # Adjust for zero-indexing

    def display_seating(self):
        for row in self.seats:
            print(' | '.join(str(passenger) if passenger else "Empty seat" for passenger in row))

    def count_open_seats(self):
        open_seats = 0
        for row in self.seats:
            for seat in row:
                if seat is None:
                    open_seats += 1
        return open_seats

    def count_food_preferences(self):
        food_counts = {}
        for row in self.seats:
            for seat in row:
                if seat:  # If seat is not None, there is a passenger
                    food_pref = seat.meal_preference
                    if food_pref in food_counts:
                        food_counts[food_pref] += 1
                    else:
                        food_counts[food_pref] = 1
        return food_counts

# Function to read from the CSV file and return the seating arrangement for a specific plane
def get_plane_seating_from_csv(plane_id, filename='bookings.csv'):
    plane_tracker = PlaneTracker(plane_id)
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Plane'] == plane_id:
                passenger = Passenger(row['Name'], row['Meal'])
                plane_tracker.add_passenger(passenger, int(row['Row']), int(row['Seat']))
    return plane_tracker

# Main loop for user interaction
while True:
    plane_id_input = input("Enter the plane ID number or 'exit' to quit: ")
    if plane_id_input.lower() == 'exit':
        break

    plane_tracker = get_plane_seating_from_csv(plane_id_input)
    print(f"\nSeating for plane ID {plane_id_input}:")
    plane_tracker.display_seating()

    open_seats = plane_tracker.count_open_seats()
    print(f"\nThere are {open_seats} open seats.")

    # After getting the plane seating from CSV, count the food preferences
    food_counts = plane_tracker.count_food_preferences()
    print("\nFood preference counts:")
    for food, count in food_counts.items():
        print(f"{food}: {count}")

    print("\n")  # Add some space before the next prompt
