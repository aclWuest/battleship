from .utils import extract_instructions, extract_coordinates, in_board, on_ship
import copy


def process_operations(ships, operations, board_size):
    """
    Processes the operations on the ships.

    Args:
    ships (list): A list of Ship objects.
    operations (list): A list of operation strings.
    board_size (int): The size of the game board.

    Raises:
    ValueError: If there is an error processing an operation.
    """
    ship_map = {ship.id: ship for ship in ships}
    for op in operations:
        try:
            coord_part = op.split(')')[0] + ')'
            ship_id = extract_coordinates(coord_part)
            ship = ship_map.get(ship_id)

            if ship is None:
                print(f"No ship with this ID {ship_id}")
                continue

            if ship.sunk:
                print(f"Ship {ship_id} is already sunk")
                continue

            if len(op) == len(coord_part):
                ship.sunk = True
            else:
                instructions = op[len(coord_part):].strip()
                handle_movement(ship, instructions, ship_map, board_size)

        except ValueError as e:
            print(f"Error processing operation '{op}': {e}")



def handle_movement(ship, instructions, ship_map, board_size):
    """
    Handles the movement and rotation of a ship.
    If a move leads to ending up outside of the board this single move is cancelled. 
    If a series of move leads to an occupy cell all the moves from the series is cancelled.

    Args:
    ship (Ship): The ship to move.
    instructions (str): The movement and rotation instructions.
    ship_map (dict): A dictionary mapping ship IDs to Ship objects.
    board_size (int): The size of the game board.
    """    
    temp_ship = copy.copy(ship)
    for move in extract_instructions(instructions):
        if move == 'M':
            next_x, next_y = calculate_next_position(ship)
            if in_board( next_x, next_y, board_size):
                ship.move(next_x, next_y)
        else:
            ship.rotate(move)
    if on_ship(ship_map.values(), next_x, next_y, board_size, ship):
        ship.x = temp_ship.x
        ship.y = temp_ship.y
        ship.orientation = temp_ship.orientation
        print(f"Two ships cannot be on the same cell: ({next_x},{next_y})")

def calculate_next_position(ship):
    """
    Calculates the ship's next position based on its current orientation.

    Args:
    ship (Ship): The ship for which to calculate the next position.

    Returns:
    tuple: A tuple (next_x, next_y) representing the next position of the ship.
    """
    direction_offsets = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    dx, dy = direction_offsets[ship.orientation]
    return ship.x + dx, ship.y + dy
