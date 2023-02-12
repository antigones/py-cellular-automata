import numpy as np
from copy import deepcopy


class LangtonsAnt:

    def __init__(self, size, n_iterations=1000, heading='e'):
        self.size = size
        self.n_iterations = n_iterations
        self.grid = np.ones((self.size, self.size)) * 255
        self.starting_point = (self.size // 2, self.size // 2)
        self.grid[self.starting_point] = 0
        cardinal_points = ['n','e','s','w']
        self.heading_idx = cardinal_points.index(heading)
        self.neighbors_idxs = [
            (-1, 0),   # n
            (0,  1),   # e
            (1,  0),   # s
            (0, -1),   # w
            ]
        self.steps = []

    def run(self):
        """
        - At a white square, turn 90° clockwise, flip the color of the square, move forward one unit
        - At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit
        """
        for _ in range(self.n_iterations):
            
            if self.grid[self.starting_point] == 255:
                # white, 90 clockwise       
                self.heading_idx = (self.heading_idx + 1) % 4
                self.grid[self.starting_point] = 0
            else:
                # back 90 ccwise     
                self.heading_idx = (self.heading_idx - 1) % 4
                self.grid[self.starting_point] = 255

            # step, updating starting point toward position
            self.starting_point = (self.starting_point[0] + self.neighbors_idxs[self.heading_idx][0], 
                                    self.starting_point[1] + self.neighbors_idxs[self.heading_idx][1])
            self.steps.append(deepcopy(self.grid))
        return self.steps