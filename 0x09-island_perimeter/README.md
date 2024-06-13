## Island perimeter
# 0. Island Perimeter
mandatory

Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

grid is a list of list of integers:

0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
ngrid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water

There is only one island (or nothing).

The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

  guillaume@ubuntu:~/0x09$ 
  guillaume@ubuntu:~/0x09$ ./0-main.py
  12
  guillaume@ubuntu:~/0x09$ 


  ## Solution

  # Island Perimeter

## Description
This project contains a Python script to calculate the perimeter of an island in a grid. The grid is a rectangular grid where `0`s represent water and `1`s represent land. Each cell is a square with a side length of 1. There is only one island in the grid.

## Usage
To use the script, simply run it with Python 3.4.3 on Ubuntu 20.04 LTS. Ensure that the script is executable.

## Files
- `island_perimeter.py`: Contains the implementation of the `island_perimeter` function.
- `README.md`: This file.

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS

## Style
The code follows PEP 8 style guidelines (version 1.7).

## License
This project is licensed under the MIT License.
