from .ship import Ship
from .operations import process_operations
from .utils import extract_ship_data, validate_ship_positions



def read_input(file_name):
    """
    Reads game data from a file.

    Args:
    file_name (str): The name of the file to read from.

    Returns:
    tuple: Board size, list of Ship objects, and list of operations.

    Raises:
    Exception: If there is an error reading from the file.
    """
    try:
        with open(file_name, 'r') as file:

            lines = file.readlines()
            board_size = int(lines[0].strip())
            ships_data = extract_ship_data(lines[1])
            ships = [Ship(s[0],s[1],s[2]) for s in ships_data]
            validate_ship_positions(ships, board_size)
            operations = [line.strip() for line in lines[2:]]

            return board_size, ships, operations
    except Exception as e:
        print(f"Error reading input file: {e}")
        exit(1)

def write_output(file_name, ships):
    """
    Writes the final state of ships to a file.

    Args:
    file_name (str): The name of the file to write to.
    ships (list): A list of Ship objects.
    """
    with open(file_name, 'w') as file:
        for ship in ships:
            file.write(f"{ship}\n")


def main(input_file, output_file):
    size, ships, operations = read_input(input_file)
    process_operations(ships, operations, size)
    write_output(output_file, ships)

if __name__ == "__main__":
    main('input.txt', 'output.txt')
