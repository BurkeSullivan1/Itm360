class Player:
    MAX_POSITION = 10  # Class attribute for max position
    MAX_SPEED = 3  # Class attribute for max speed

    def __init__(self, position=0, speed=0):
        # Set the player's position, ensuring it does not exceed MAX_POSITION
        self.position = min(position, Player.MAX_POSITION)
        # Set the player's speed, ensuring it does not exceed MAX_SPEED
        self.speed = min(speed, Player.MAX_SPEED)

    def position_notice(self):
        # Method to return a notice about the player's maximum position
        return f"Player max position is {Player.MAX_POSITION}"

# Print Player.MAX_POSITION
print(Player.MAX_POSITION)

# Create two Player objects p1 and p2
p1 = Player()
p2 = Player()

# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)  # This accesses the class attribute through the instance
print(p2.MAX_SPEED)  # Same here

# Assign 7 to p1.MAX_SPEED. This creates an instance attribute for p1
p1.MAX_SPEED = 7

# Print p1.MAX_SPEED, p2.MAX_SPEED, and Player.MAX_SPEED
print(p1.MAX_SPEED)  # This will print 7 because we assigned it to the p1 instance
print(p2.MAX_SPEED)  # This will still print 3 because p2's class attribute is unchanged
print(Player.MAX_SPEED)  # This will print 3 because the class attribute itself is unchanged

# Note: Assigning a value to an instance attribute named like a class attribute
# does not change the class attribute. Instead, it shadows the class attribute
# with a new instance attribute for that particular instance.