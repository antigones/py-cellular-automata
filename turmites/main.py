import numpy as np
from PIL import Image
import imageio
from turmite import Turmite

# 120080 Langton's ant
# 021121181180 snowflake-ish
# 181181121010 Fibonacci spiral
turmite = Turmite(size=100, rule='181181110012081111', n_iterations=2000)
steps = turmite.run()

normalized_steps = [list(map(lambda x: list(map(lambda y: y * 255, x)), img)) for img in steps]
imgs = [Image.fromarray(np.array(img).astype(np.uint8)) for img in normalized_steps]

imageio.mimsave('turmite.gif', imgs[1500:])