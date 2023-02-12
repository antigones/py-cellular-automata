import random as rd

class CellularAutomaton:

    def __init__(self, rule, n_iterations=300, random_seed=False):
        self.configurations = range(7, -1, -1)
        self.rule = rule
        self.random_seed = random_seed
        self.width = n_iterations * 2

        self.bin_rule = format(rule, '08b')
        self.input_output = self.create_dict(self.bin_rule)
        self.n_iterations = n_iterations
        
    def create_dict(self, bin_rule):
        d = {}
        for i, configuration in enumerate(self.configurations):
            d[configuration] = int(bin_rule[i])
        return d

    def generate(self):
        # rd.seed(42)
        
        max_len = 2 ** self.width
        if self.random_seed:
            input = rd.randint(0, max_len)
        else:
            input = 2 ** (self.width // 2)

        steps = []
        bin_format = '0' + str(max_len.bit_length()) + 'b'
        steps.append([int(x) for x in format(input, bin_format)])

        for i in range(self.n_iterations):
            mask = 7 # 111
            n = 0
            # start from LSB
            for i in range(self.width):
                o = input & mask
                k = o >> i
                n += self.input_output[k] * (2 ** (i + 1)) # center pixel, so index is i+1
                mask = mask << 1
            steps.append([int(x) for x in format(n, bin_format)])
            input = n
            
        return steps