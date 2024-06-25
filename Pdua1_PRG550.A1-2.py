# program: Pdua1_PRG550.A1.py
# my.seneca id:  Pdua1
# course code: PRG550 NCCL
# current semester: 5th sem
# date:    October 01, 23
# purpose: python program for PRG550 Assignment #1

import copy
import random
import string


def load_maze(maze_str):
    maze = []
    for row in maze_str.split('\n'):
        if row:
            maze.append(list(row))
    return maze


class MazeSolver:
    def __init__(self, maze_str):
        self.maze = load_maze(maze_str)
        self.rows = len(self.maze)
        self.cols = len(self.maze[0])
        self.directions = [(0, 1), (1, 0)]
        self.visited_cells = [[False] * self.cols for _ in range(self.rows)]
        self.path = None

    def solve(self):
        start = (1, 0)
        self.visited_cells[start[0]][start[1]] = True
        stack = [(start, 'E', 0)]

        while stack:
            current, path, path_length = stack.pop()
            r, c = current

            for dr, dc in self.directions:
                new_r, new_c = r + dr, c + dc

                if self.is_valid_cell(new_r, new_c) and not self.visited_cells[new_r][new_c] and self.maze[new_r][
                    new_c] == ' ':
                    stack.append(((new_r, new_c), path + ('E' if dc == 1 else 'S'), path_length + 1))
                    self.visited_cells[new_r][new_c] = True

                if self.maze[new_r][new_c] == '#':
                    self.path = path
                    return

    def is_valid_cell(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def print_maze(self):
        for row in self.maze:
            print(''.join(row))

    def print_solution(self):
        self.print_maze()
        print(f'Maze dimensions:   {self.rows - 2}x{self.cols - 2}')

        found_coords = self.find_symbol_coords('#')
        if found_coords:
            print(f'Found # at coords: {found_coords[0]},{found_coords[1]}')
        else:
            print('The maze does not contain the # symbol.')

        print(f'Path:              {self.path}')
        total_searches = len(self.path)
        total_tiles = sum(row.count(' ') for row in self.maze) - 2  # Exclude border walls
        percentage = (total_searches / total_tiles) * 100
        print(f'Total searches:    {total_searches}/{total_tiles} {percentage:.4f}% of maze')

    def find_symbol_coords(self, symbol):
        for r, row in enumerate(self.maze):
            for c, cell in enumerate(row):
                if cell == symbol:
                    return r, c
        return None


def main():
    maze1 = '''-------------------+
@                  |
| | --+ | | -------+
| |   | | |      # |
| +-+ | | +-+ | ---+
|   | | |   | |    |
| | | +-+ | +-+----+
| | |   | |        |
| | |   | |        |
+-+-+---+-+--------+'''

    maze2 = '''-------------------------------+
@                              |
| --+ --+ --+ | --------+ | |  |
|   |   |   | |         | | |  |
| --+---+-+ | +-+ | | | +-+ |  |
|         | |   | | | |   | |  |
| ------+ | | | | | | | | +-+  |
|       | | |#| | | | | |   |  |
| ------+ +-+ | +-+-+-+ +-+ +--+
|       |   | |       |   |    |
| --+ --+ --+ +-----+ +-+ +-+  |
|   |   |   |       |   |   |  |
| --+ | | --+-+ | --+ | | | |  |
|   | | |     | |   | | | | |  |
| | +-+ | | | +-+ --+ | +-+ |  |
| |   | | | |   |   | |   | |  |
| | --+-+ +-+---+ --+-+ | +-+--+
| |     |       |     | |      |
| +---+ | ------+-+ --+ | --+  |
|     | |         |   | |   |  |
| ----+ +-+ | --+ +-+ | | --+--+
|     |   | |   |   | | |      |
+-----+---+-+---+---+-+-+------+'''

    maze3 = '''-------------------+
@  #               |
| --+ | | | ----+  |
|   | | | |     |  |
| --+ | +-+ | | |  |
|   | |   | | | |  |
| | +-+-+ | | | +--+
| |     | | | |    |
| |     | | | |    |
+-+-----+-+-+-+----+'''

    maze4 = '''--------------------+
@                   |
| | ----------------+
| |#                |
| | | ----+ ----+ |
| | |    #|    | |
| | | | ----+-+ | |
| | | |       | | |
| | | | | ----+ | |
| | | | |        | |
| | | | | | ----+-+ |
| | | | | |        | |
| | | | | | | ----+ |
| | | | | | |#      |
| | | | | | | | ----+
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
+-+ +-+ +-+ +-+ +-+'''

    mazes = [maze1, maze2, maze3, maze4]

    for idx, maze in enumerate(mazes):
        print(f"Maze {idx + 1}:")
        maze_solver = MazeSolver(maze)
        maze_solver.solve()
        maze_solver.print_solution()
        print("\n" + "=" * 20 + "\n")


if __name__ == '__main__':
    main()
