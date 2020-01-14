from PIL import Image
import os

size = (640, 640)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size)
        i.save('pngsSize/{}Size{}'.format(fn, fext))
