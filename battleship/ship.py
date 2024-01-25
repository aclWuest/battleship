class Ship:
    """
    A class to represent a ship.

    Attributes:
    id (tuple): The initial position of the ship, used as an identifier.
    x (int): The x-coordinate of the ship.
    y (int): The y-coordinate of the ship.
    orientation (str): The orientation of the ship ('N', 'E', 'S', 'W').
    sunk (bool): Flag to indicate if the ship is sunk.
    """
    def __init__(self, x, y, orientation):
        self.id = (x, y)  
        self.x = x
        self.y = y
        self.orientation = orientation
        self.sunk = False

    def __repr__(self):
        status = "SUNK" if self.sunk else ""
        return f"({self.x}, {self.y}, {self.orientation}) {status}".strip()

    def rotate(self, direction):
        """
        Rotates the ship in the given direction.

        Args:
        direction (str): The direction to rotate ('L' for left, 'R' for right).
        """
        orientations = "NESW"
        idx = orientations.index(self.orientation)
        if direction == 'L':
            self.orientation = orientations[(idx - 1) % 4]
        elif direction == 'R':
            self.orientation = orientations[(idx + 1) % 4]

    def move(self, next_x, next_y):
        self.x = next_x
        self.y = next_y

