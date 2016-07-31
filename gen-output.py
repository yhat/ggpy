import os


master = [os.path.join("testing/master", f) for f in os.listdir("testing/master")]
master.sort(key=lambda x: float(x[24:-4]))

schmeing = [os.path.join("testing/schmeing", f) for f in os.listdir("testing/schmeing")]
schmeing.sort(key=lambda x: float(x[24:-4]))

def img(f):
    return "<img src='{filename}' style='max-width: 40%; display: inline-block;' />".format(filename=f)

with open("test.html", "wb") as f:
    f.write("<html>\n<body>\n")
    for f1, f2 in zip(master, schmeing):
        f.write("<div>\n\t" + img(f1))
        f.write("\n\t" + img(f2) + "\n</div>\n")
    f.write("</body>")
