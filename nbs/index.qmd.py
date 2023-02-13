"""---
title: Home
pagetitle: nbdev – Create delightful software with Jupyter Notebooks
page-layout: custom
section-divs: false
css: index.css
toc: false
image: https://nbdev.fast.ai/images/card.png
description: Write, test, document, and distribute software packages and technical articles — all in one place, your notebook.
---"""

from fastcore.foundation import L
from nbdev import qmd


def img(fname, classes=None, **kwargs): return qmd.img(f"images/{fname}", classes=classes, **kwargs)


def btn(txt, link): return qmd.btn(txt, link=link,
                                   classes=['btn-action-primary', 'btn-action', 'btn', 'btn-success', 'btn-lg'])


def banner(txt, classes=None, style=None): return qmd.div(txt, L('hero-banner') + classes, style=style)


def testm(im, nm, detl, txt):
    return qmd.div(f"""{img(im, link=True)}

# {nm}

## {detl}

### {txt}""", ["testimonial", "g-col-12", "g-col-md-6"])


def feature(im, desc): return qmd.div(f"{img(im + '.svg')}\n\n{desc}\n",
                                      ['feature', 'g-col-12', 'g-col-sm-6', 'g-col-md-4'])


def b(*args, **kwargs): print(banner(*args, **kwargs))


def d(*args, **kwargs): print(qmd.div(*args, **kwargs))


###
# Output section
###

b(f"""# <span style='color:#009AF1'>Create delightful software</span><br>with Jupyter Notebooks

### Write, test, document, and distribute software packages and technical articles — all in one place, your notebook.

{btn('Get started', '/getting_started.ipynb')}

{img('card.png', style={"margin-top": "40px", "margin-bottom": "40px"}, link=True)}""", "content-block")

b(f"""## Get started in seconds

{btn('Install nbdev', '/getting_started.ipynb')}""", 'content-block', style={"margin-top": "40px"})
