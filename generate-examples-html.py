from sh import find
import json
from datetime import datetime
import os
import sys

rows = []
for f in find("docs/" + sys.argv[1]):
    f = f.strip()
    if f.endswith('.ipynb')==False or ".ipynb_checkpoints" in f:
        continue
    ipynb = json.load(open(f, 'rb'))


    html = """
<div class="col-sm-3">
    <div class="panel panel-default">
      <div class="panel-heading">
        <h3 class="panel-title text-center">
          <a href="{url}">{title}</a>
        </h3>
      </div>
      <div class="panel-body">
        <a href="{url}">
          <img src="{img}" style="height: 200px; width: 100%" />
        </a>
      </div>
    </div>
</div>
    """

    for cell in ipynb['cells']:
        if cell.get("outputs"):
            outputs = cell["outputs"]
            for output in outputs:
                if "image/png" in output['data']:
                    png = output['data']['image/png'].replace('\n', '')
                    url = "build/docs/" + sys.argv[1] + "/" + os.path.basename(f).replace(".ipynb", ".html")
                    url = "notebook.html?page=" + url
                    title = os.path.basename(f)[:-6]
                    img = "data:image/png;base64,%s" % png
                    rows.append(html.format(title=title, img=img, url=url))
                    break

layout = open("template.html", "rb").read()
buildtime = datetime.now().strftime("%Y-%m-%d")
print layout.format(body="\n".join(rows), buildtime=buildtime)
