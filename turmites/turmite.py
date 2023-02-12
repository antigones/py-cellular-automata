import numpy as np
from copy import deepcopy


class Turmite:

    def __init__(self, size, n_iterations=1000):
        self.size = size
        self.n_iterations = n_iterations
        self.grid = np.zeros((self.size, self.size))
        self.starting_point = (self.size // 2, self.size // 2)
        self.grid[self.starting_point] = 0
        
        self.state = 0
    
        self.heading_idx = 0

        self.neighbors_idxs = [
            (-1, 0),   # n
            (0,  1),   # e
            (1,  0),   # s
            (0, -1),   # w
            ]
        
        self.steps = []


    def run(self):
     
        for _ in range(self.n_iterations):
            current_color = self.grid[self.starting_point]

            if current_color == 0:
                if self.state == 0:
                    self.grid[self.starting_point] = 255
                    self.heading_idx = (self.heading_idx + 1) % 4
                if self.state == 1:
                    self.grid[self.starting_point] = 0
                self.state = 0         

            if current_color == 255:
                if self.state == 0:
                    self.grid[self.starting_point] = 255
                    self.heading_idx = (self.heading_idx + 1) % 4
                if self.state == 1:
                    self.grid[self.starting_point] = 0 
                self.state = 1

            # step, updating starting point toward position
            self.starting_point = (self.starting_point[0] + self.neighbors_idxs[self.heading_idx][0], 
                                    self.starting_point[1] + self.neighbors_idxs[self.heading_idx][1])
            self.steps.append(deepcopy(self.grid))
        return self.steps