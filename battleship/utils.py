import re

class ExtractionError(Exception):
    """Custom exception for errors in data extraction."""
    pass

def extract_coordinates(string):
    """
    Extracts and returns a tuple of integers from a coordinate string.
    
    Args:
    string (str): A string in the format '(x, y)'.

    Returns:
    tuple: A tuple of two integers representing coordinates.

    Raises:
    ExtractionError: If the string format is invalid.
    """
    if not re.match(r'^\(\d+, \d+\)$', string):
        raise ExtractionError(f"Invalid coordinate format: '{string}'")
    numbers = string.strip("()").split(", ")
    return tuple(map(int, numbers))

def extract_instructions(string):
    """
    Extracts every second character from a the instructions string.
    
    Args:
    string (str): A string from which to extract characters.

    Returns:
    list: A list of characters extracted from the string.

    Raises:
    ExtractionError: If the input is not a string or the format is invalid.
    """
    if not isinstance(string, str) or not re.match(r'^M([LRM]M?)*$', string):
        raise ExtractionError(f"Invalid instruction format: '{string}'")
    return [string[i] for i in range(1, len(string), 2)]

def extract_ship_data(string):
    """
    Extracts ship data from a string.

    Args:
    string (str): A string containing ship data in the format '(x, y, orientation)'.

    Returns:
    list: A list of tuples with ship coordinates and orientation.

    Raises:
    ExtractionError: If no valid ship data is found or the format is invalid.
    """
    pattern = r'\((\d+), (\d+), ([NESW])\)'
    matches = re.findall(pattern, string)
    if not matches:
        raise ExtractionError("No valid ship data found.")
    for x, y, orientation in matches:
        if not (0 <= int(x) and 0 <= int(y) and orientation in "NESW"):
            raise ExtractionError(f"Invalid ship data: '({x}, {y}, {orientation})'")
    return [(int(x), int(y), orientation) for x, y, orientation in matches]

def validate_ship_positions(ships, board_size):
    """
    Validates that all ships are within the board and no duplicate positions exist.

    Args:
    ships (list): A list of Ship objects.
    board_size (int): The size of the board (assumed to be a square).

    Returns:
    bool: True if all validations pass.

    Raises:
    ValueError: If a ship is out of bounds or if duplicate positions are found.
    """
    seen_positions = set()

    for ship in ships:
        if not (0 <= ship.x < board_size and 0 <= ship.y < board_size):
            raise ValueError(f"Ship position out of board bounds: ({ship.x}, {ship.y})")

        if (ship.x, ship.y) in seen_positions:
            raise ValueError(f"Duplicate ship position detected: ({ship.x}, {ship.y})")

        seen_positions.add((ship.x, ship.y))

def in_board(next_x, next_y, board_size):
    """
    Checks if the given coordinates are within the boundaries of the board.

    Args:
    next_x (int): The x-coordinate to check.
    next_y (int): The y-coordinate to check.
    board_size (int): The size of the board.

    Returns:
    bool: True if the coordinates are within the board, False otherwise.
    """
    if not (0 <= next_x < board_size and 0 <= next_y < board_size):
        return False  
    
    return True  

def on_ship(ships, next_x, next_y, board_size ,ship_to_move):
    """
    Checks if the given coordinates collide with any non-sunk ship, excluding the ship that is moving.

    Args:
    ships (list): A list of Ship objects.
    next_x (int): The x-coordinate to check.
    next_y (int): The y-coordinate to check.
    board_size (int): The size of the board.
    ship_to_move (Ship): The ship that is being moved.

    Returns:
    bool: True if moving to the coordinates would result in a collision, False otherwise.
    """
    ship_positions = {(ship.x, ship.y) for ship in ships if not ship.sunk and ship != ship_to_move}

    if (next_x, next_y) in ship_positions:
        return True 

    return False 