"""---
pagetitle: My Projects
section-divs: false
page-layout: full
toc: false
listing:
  contents: Project_index/
  sort: date desc
  type: default
  categories: true
  sort-ui: false
  filter-ui: false
title-block-banner: true
---"""

from fastcore.foundation import L
from nbdev import qmd

projects = L(
    ('mail.png', 'Project Name', 'Long Name', 'Description'),
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

projects_d = qmd.div('\n'.join(projects.starmap(testm)), ['content-block', 'grid', 'gap-6'])

def feature(im, desc): return qmd.div(f"{img(im+'.svg')}\n\n{desc}\n", ['feature', 'g-col-12', 'g-col-sm-6', 'g-col-md-4'])

def b(*args, **kwargs): print(banner (*args, **kwargs))
def d(*args, **kwargs): print(qmd.div(*args, **kwargs))

###
# Output section
###


