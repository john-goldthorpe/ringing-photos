"""
make_thumbnails.py

JMG
08-MAY-2020
"""

from PIL import Image
import glob
from pathlib import Path

for filename in glob.glob('*.jpg'):
    if 'thumb' in filename:
        continue
    thumb_filename = filename[:-4] + '_thumb.jpg'
    if Path(thumb_filename).exists():
        continue
    im = Image.open(filename)
    im.thumbnail((256, 256), Image.ANTIALIAS)
    im.save(thumb_filename, 'JPEG')
