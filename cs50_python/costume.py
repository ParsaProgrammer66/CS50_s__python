import sys
from PIL import image

images = []
for arg in sys.argv:
    image = image.open(arg)
    images.append(image)

images[0].save(
    "costume.gif",save_all=True,append_images=[images[1]],duration=200,loop=0)
