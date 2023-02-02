import imageio
from cellular_automaton import CellularAutomaton

ca = CellularAutomaton(rule=90, n_iterations=100, random_seed=False)
img = ca.generate()
imageio.imsave('ca_output.gif', img)