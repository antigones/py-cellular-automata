import numpy as np
from PIL import Image
import imageio
from langton.langtons_ant import LangtonsAnt

ant = LangtonsAnt(size=300, n_iterations=1000, heading='e')
steps = ant.run()

imgs = [Image.fromarray(img.astype(np.uint8)).resize((800,800), Image.Resampling.BOX) for img in steps]
# duration is the number of milliseconds between frames; this is 40 frames per second

imageio.mimsave('new.gif', imgs)
# imageio.mimsave('new1.gif', steps[12000:])