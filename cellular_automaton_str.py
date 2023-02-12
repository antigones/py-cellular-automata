import numpy as np


class CellularAutomaton:

    def __init__(self, rule, n_iterations=300, random_seed=False):
        self.configurations = ["111", "110", "101", "100", "011", "010", "001", "000"]
        self.rule = rule
        self.random_seed = random_seed

        self.bin_rule = format(rule, '08b')
        self.input_output = self.create_dict(self.bin_rule)
        self.n_iterations = n_iterations

    def create_dict(self, bin_rule):
        d = {}
        for i, configuration in enumerate(self.configurations):
            d[configuration] = bin_rule[i]
        return d

    def generate(self):
        row_format = "0{row_content}0"
        if self.random_seed:
            input = "".join(np.random.randint(0, 2, 2*self.n_iterations+1).astype(str))
        else:
            seed = "1"
            input = self.n_iterations * "0" + seed + self.n_iterations * "0"
            input = row_format.format(row_content = input)
        out_list = []
        out_list.append([int(x)*255 for x in input])
        for _ in range(self.n_iterations):
            next_iteration = []
            for i in range(len(input)-2):
                next_iteration.append(self.input_output[input[i:i+3]])
            input = row_format.format(row_content = "".join(next_iteration))
            out_list.append([int(x)*255 for x in input])
        return out_list