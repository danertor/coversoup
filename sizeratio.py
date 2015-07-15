from __future__ import print_function
import os, sys
from PIL import Image

ratio_threshold = 1.1 
list = ['C:\\cygwin\\home\\XI316270\\python\\image_comparison\\images\\sample_03.jpg','C:\\cygwin\\home\\XI316270\\python\\image_comparison\\images\\sample_04.jpg']
for infile in list:
    try:    
        im = Image.open(infile)
        xsize, ysize = im.size
        ratio_status = "good" if xsize / ysize <= ratio_threshold and xsize / ysize > 1 / ratio_threshold  else "bad"
        print(infile, ratio_status, xsize / ysize) 
    except IOError:
        print("cannot read", infile)
