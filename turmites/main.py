import numpy as np
from PIL import Image
import imageio
from turmite import Turmite

# 120080 Langton's ant

turmite = Turmite(size=200, rule='181181121010', n_iterations=10000)
steps = turmite.run()

imgs = [Image.fromarray(np.array(img)) for img in steps]
# duration is the number of milliseconds between frames; this is 40 frames per second

imageio.mimsave('new.gif', imgs)
imageio.mimsave('new1.gif', imgs[8342:])