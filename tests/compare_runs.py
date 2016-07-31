import os
import sys
import imgdiff
import tempfile
import operator
import math
from PIL import Image

rundir1 = sys.argv[1]
rundir2 = sys.argv[2]
html = """
<html>
    <head>
        <style>
            img {
                max-width: 80%;
                display: inline-block;
            }
        </style>
    </head>
    <body>
"""

def calc_mse(image1, image2):
    h1 = Image.open(image1).histogram()
    h2 = Image.open(image2).histogram()
    return math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))

outputdir = tempfile.mkdtemp("-ggplot-test")
for img in os.listdir(rundir1):
    img1 = os.path.join(rundir1, img)
    img2 = os.path.join(rundir2, img)
    mse = calc_mse(img1, img2)
    f = os.path.join(outputdir, img)
    imgdiff.main([None, img1, img2, "-S", "-o", f])
    div = """
<div>
    <p>%s - %f</p>
    <img src='%s' />
    <p>%s vs. %s</p>
</div>""" % (img, mse, f, img1, img2)
    html += div


html += "\n</body>"
print html
