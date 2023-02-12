from copy import deepcopy


class Turmite:

    def __init__(self, size, rule, n_iterations=1000):
        """
                                current-color = 0    current-color = 1
            current-state = 0              1,8,1                1,8,1
            current-state = 1              1,2,1                0,1,0

            The {1,8,1} triple therefore states that the colour should change to 1, 
            turn left (8) and adopt state 1 before moving forwards.

            The direction to turn is specified by:

            1: no turn
            2: right
            4: u-turn
            8: left
        """

        self.size = size
        self.n_iterations = n_iterations
        self.grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.starting_point = (self.size // 2, self.size // 2)
        self.grid[self.starting_point[0]][self.starting_point[1]] = 0
        
        self.state = 0
    
        self.heading_idx = 0

        self.neighbors_idxs = [
            (-1, 0),   # n
            (0,  1),   # e
            (1,  0),   # s
            (0, -1),   # w
            ]

        """
            how much to advance in neighbors_idx to make that move
        """
        
        self.move_kind_to_idx = {
                                    1: 0,
                                    2: 1,
                                    4: 2,
                                    8: -1
                                }
                            
        self.rule = rule
        self.states_and_rules = self.parse_rule()
        self.steps = []

    def parse_rule(self):
        
        parts = [self.rule[i:i+3] for i in range(0, len(self.rule), 3)]
        states_and_rules = [parts[i:i+2] for i in range(0, len(parts), 2)]
        
        return states_and_rules


    def run(self):
     
        for _ in range(self.n_iterations):
            current_color = self.grid[self.starting_point[0]][self.starting_point[1]]
            write_color, move_kind, new_state = self.states_and_rules[self.state][current_color]
            self.grid[self.starting_point[0]][self.starting_point[1]] = int(write_color)
            self.heading_idx = (self.heading_idx + self.move_kind_to_idx[int(move_kind)]) % 4
            self.state = int(new_state)
            self.starting_point = (self.starting_point[0] + self.neighbors_idxs[self.heading_idx][0], 
                                    self.starting_point[1] + self.neighbors_idxs[self.heading_idx][1])

            self.steps.append(deepcopy(self.grid))
        return self.steps