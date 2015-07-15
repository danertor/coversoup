from __future__ import print_function
import os, sys
from PIL import Image

size = (500,500)
list = ['C:\\cygwin\\home\\XI316270\\python\\image_comparison\\images\\sample_03.jpg','C:\\cygwin\\home\\XI316270\\python\\image_comparison\\images\\sample_04.jpg']
for infile in list:
    f, e = os.path.splitext(infile)
    print(f) 
    outfile = f + "_out" + ".jpg"
    if infile != outfile:
        try:    
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot convert", infile)
