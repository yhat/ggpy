from sh import find
import json
from datetime import datetime
import os
import sys

rows = []
for f in find("docs/geoms"):
    f = f.strip()
    if f.endswith('.ipynb')==False or ".ipynb_checkpoints" in f:
        continue
    ipynb = json.load(open(f, 'rb'))


    html = """<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>ggplot | Documentation</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <link rel="stylesheet" href="public/css/bootstrap.css" media="screen">
      <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
      <!--[if lt IE 9]>
        <script src="../bower_components/html5shiv/dist/html5shiv.js"></script>
        <script src="../bower_components/respond/dest/respond.min.js"></script>
      <![endif]-->
      <style>
        pre {
            line-height: 1;
        }
      </style>
    </head>
    <body>
    <div class="container">
    """
    print html

    for cell in ipynb['cells']:
        if cell['source']:
            html = "<pre>" + "\n".join(cell['source']) + "</pre>"
            print "<div class='row'>" + html + "</div>"
        if cell["outputs"]:
            outputs = cell["outputs"]
            for output in outputs:
                if "image/png" in output['data']:
                    png = output['data']['image/png'].replace('\n', '')
                    img = "data:image/png;base64,%s" % png
                    html = '<img src="' + img + '" width="80%" />'
                if "text/plain" in output['data']:
                    text = output['data']['text/plain']
                    html = "<code>" + html + "</code>"
                if "text/html" in output['data']:
                    html = "\n".join(output['data']['text/html'])
                    html = html.replace('class="dataframe"', 'class="table table-bordered"')
                print "<div class='row'>" + html + "</div>"

    print "<p class='lead'>%s</p>" % f
    print "</div></body>"
    break

# layout = open("template.html", "rb").read()
# buildtime = datetime.now().strftime("%Y-%m-%d")
# print layout.format(body="\n".join(rows), buildtime=buildtime)
