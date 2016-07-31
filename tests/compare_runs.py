import os
import sys
import imgdiff
import tempfile
import operator
import math
from PIL import Image
import pandas as pd

rundir1 = sys.argv[1]
rundir2 = sys.argv[2]
html = """
<html>
    <head>
        <link rel="stylesheet" href="http://bootswatch.com/cosmo/bootstrap.min.css" />
        <style>
            .broken-test {
                background-color: red;
            }
            img {
                max-width: 80%;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <h1 class="text-center">ggplot visual test output</h1>
"""

def calc_mse(image1, image2):
    h1 = Image.open(image1).histogram()
    h2 = Image.open(image2).histogram()
    return math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))

outputdir = tempfile.mkdtemp("-ggplot-test")
images = os.listdir(rundir1)
images.sort(key=lambda x: os.stat(os.path.join(rundir1, x)).st_mtime)
test_results = ""
table = []
for img in images:
    img1 = os.path.join(rundir1, img)
    img2 = os.path.join(rundir2, img)
    mse = calc_mse(img1, img2)
    f = os.path.join(outputdir, img)
    imgdiff.main([None, img1, img2, "-S", "-o", f])
    if mse > 0:
        broken = "broken-test"
    else:
        broken = ""
    div = """
<div id="%s" class="text-center %s">
    <p class="lead">%s - %f</p>
    <img src='%s' />
    <p class="text-muted text-small">%s vs. %s</p>
</div><hr>""" % (img, broken, img, mse, f, img1, img2)
    test_results += div
    table.append({ 'name': os.path.basename(f), 'mse': mse })

html += "\n" + "<div class='row' style='padding-left: 25%; width: 75%;'>" + pd.DataFrame(table)[['name', 'mse']].to_html(classes='table table-bordered') + "</div>\n"
html += test_results
html += "\n</body>"
print html
