"""
make_thumbnails.py

JMG
08-MAY-2020
"""

from PIL import Image
import glob

for filename in glob.glob('*.jpg'):
    if 'thumb' in filename:
        continue
    im = Image.open(filename)
    im.thumbnail((256, 256), Image.ANTIALIAS)
    im.save(filename[:-4] + '_thumb.jpg', 'JPEG')
