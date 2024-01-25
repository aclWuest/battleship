# Battleship Game

## Overview
This is a Python implementation of the classic Battleship game. It allows you to set up a game board with ships and perform various operations such as moving ships and shooting at coordinates to sink ships.

## Project Structure
The project is organized into several files to keep the code modular and maintainable:
- `main.py`: The main script to run the Battleship game.
- `ship.py`: Contains the `Ship` class definition for representing ships.
- `utils.py`: Provides utility functions for data extraction and validation.
- `operations.py`: Contains functions for processing game operations.
- `input.txt`: An example input file for setting up the game board and operations.
- `output.txt`: The output file where the final state of ships is stored.

## Getting Started
1. Clone the repository to your local machine:

   ```shell
   git clone <repository-url>
   cd battleship-game
   ```

2. Run the Battleship game with the example input:

   ```shell
   python -m battleship.main
   ```

3. Check the `output.txt` file to see the final state of the ships after the game operations.

## Usage
- Modify the `input.txt` file to set up your own game board and operations.
- Run the Battleship game using `python -m battleship.main`.

## File Descriptions
- `main.py`: This is the main script to run the game. It reads the input file, processes game operations, and writes the final state of the ships to the output file.

- `ship.py`: Defines the `Ship` class, representing individual ships on the game board. Ships have attributes such as coordinates, orientation, and sunk status.

- `utils.py`: Provides utility functions for data extraction and validation, including functions to extract coordinates and validate ship positions.

- `operations.py`: Contains functions for processing game operations, such as moving ships, rotating, and shooting. It also includes functions to calculate the next position of a ship.

- `input.txt`: An example input file that you can modify to set up your own game board and operations. Follow the format described in the example.

- `output.txt`: The output file where the final state of ships is stored after processing the game operations.

