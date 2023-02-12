import numpy as np
from PIL import Image
import imageio
from turmite import Turmite


turmite = Turmite(size=200, n_iterations=10000)
steps = turmite.run()

imgs = [Image.fromarray(img.astype(np.uint8)) for img in steps]
# duration is the number of milliseconds between frames; this is 40 frames per second

#imageio.mimsave('new.gif', imgs, duration=1/100000)
imageio.mimsave('new1.gif', imgs[8342:])