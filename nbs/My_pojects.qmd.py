"""---
title: TEST1
pagetitle: My project list
page-layout: custom
section-divs: false
css: index.css
toc: false
description: Write page description here.
---"""

from fastcore.foundation import L
from nbdev import qmd

projects = L(
    ('forest.png', 'Project Name', 'Long Name', 'Description'),
    ('forest.png', 'Projet 2', 'Longer Name', ' Description'),
    ('forest.png', 'pjname', 'qq, dd', 'XD'),
)

def img(fname, classes=None, **kwargs): return qmd.img(f"images/{fname}", classes=classes, **kwargs)
def btn(txt, link): return qmd.btn(txt, link=link, classes=['btn-action-primary', 'btn-action', 'btn', 'btn-success', 'btn-lg'],style ={"background-color": "#c12d4a"})
def banner(txt, classes=None, style=None): return qmd.div(txt, L('hero-banner')+classes, style=style)
def testm(im, nm, detl, txt):
    return qmd.div(f"""{img(im, link=False)}

# {nm}

## {detl}

### {txt}""", ["testimonial", "g-col-12", "g-col-md-6"])

projects_d = qmd.div('\n'.join(projects.starmap(testm)), ['content-block', 'grid', 'gap-4'])

def feature(im, desc): return qmd.div(f"{img(im+'.svg')}\n\n{desc}\n", ['feature', 'g-col-12', 'g-col-sm-6', 'g-col-md-4'])

def b(*args, **kwargs): print(banner (*args, **kwargs))
def d(*args, **kwargs): print(qmd.div(*args, **kwargs))

###
# Output section
###

b(f"""# My Personal <span style='color:#c12d4a'> Projects</span><br>

### You can write here something idk what yet.

{btn('View All Projects', '/01_projects.ipynb')}

""")

projects_b = banner("## Here's are some of them")

d(projects_b+projects_d, "mid-content")

b(f"""## Temp Place

{btn('Temp Name', '/01_projects.ipynb')}""", 'content-block', style={"margin-top": "40px"})

