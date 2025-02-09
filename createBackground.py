import os
from PIL import Image, ImageDraw

os.chdir(os.path.dirname(os.path.abspath(__file__)))

bg = Image.new('RGBA', (384, 480), 'white')

bgCopy = bg.copy()

width, height = bgCopy.size

draw = ImageDraw.Draw(bgCopy)

draw.rectangle((10, 10, width-10, height-10), fill='white', outline='black')

flowers = Image.open('invTempSmall.png')

bgCopy.paste(flowers, (0, 0), flowers)

bgCopy.save('template.png')