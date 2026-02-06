import numpy as np
from numpy import random as r


class Grid:

    def __init__(self, x_dim, y_dim, num_states=2):
        self.size = (x_dim, y_dim)
        self.grid = np.zeros((x_dim, y_dim))
        self.num_states = num_states  # The number of possible states. E.g., in GOL there are 2 states: on and off.
        self.rules = []

    def get_grid(self):  # Returns the entire grid matrix.
        return self.grid

    def get_size(self):  # Returns the dimensions of the cell grid.
        return self.size

    def get_state(self, x, y):  # Returns the state of the cell at (x, y).
        return self.grid[x][y]

    def get_neighbors(self, x, y):  # Returns list of neighbor coordinates and their states.
        neighbors = []
        for i in range(3):
            u = (x - 1 + i) % self.size[0]
            for j in range(3):
                v = (y - 1 + j) % self.size[1]
                if (i != 1) or (j != 1):
                    state = self.get_state(u, v)
                    if state != 0:
                        neighbors.append((u, v, state))
        return neighbors

    def get_active(self):
        active = []
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.get_state(x, y) != 0:
                    active.append((x, y, self.get_state(x, y)))
        return active

    def add_rule(self, b, s, area):  # Adds a rule for a specified list of cells. b and s must be lists.
        self.rules.append((b, s, area))

    def randomize(self, num_cells):  # Randomizes the grid with a specified number of cells.
        for i in range(num_cells):
            x, y = r.randint(0, self.size[0]), r.randint(0, self.size[1])
            self.grid[x, y] = 1

    def evolve(self):
        next_grid = np.zeros(self.size)
        for rule in self.rules:  # For each rule (each area)
            b, s, area = rule  # Unpack the rule into born, stay, and the list of cells defining the area.
            for cell in area:
                x, y = cell
                num_neighbors = len(self.get_neighbors(x, y))
                print(num_neighbors)
                if self.get_state(x, y) == 1:
                    if num_neighbors in s:
                        next_grid[x][y] = 1
                    else:
                        next_grid[x][y] = 0
                else:
                    if num_neighbors in b:
                        next_grid[x][y] = 1
                    else:
                        next_grid[x][y] = 0
        self.grid = next_grid
