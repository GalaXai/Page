"""---
pagetitle: Page
section-divs: false
css: styles.css
toc: false
image: images/profile.jpg
about:
  template: jolla
  image-width: 20em
  image-shape: round
sidebar: false
---"""

from fastcore.foundation import L
from nbdev import qmd


def img(fname, classes=None, **kwargs): return qmd.img(f"images/{fname}", classes=classes, **kwargs)


def btn(txt, link): return qmd.btn(txt, link=link,
                                   classes=['btn-action-primary', 'btn-action', 'btn', 'btn-success', 'btn-lg'],style ={"background-color": "#c12d4a","border-color":"#c12d4a"})

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


b(f"""# <span style='color:#009AF1'>Hello </span><br>Welcome to my Page 👋

Hello,I am aspiring Data Scientist/Software Enginer, Today second year Computer Science, currently exploring Deep Learning Area. Althought i may not have any commercial experience, I have been having fun with Deep Learning concepts
and made some small projects most of them can be found on my kaggle profile, or by going to the Projects tab
My most significant project can be found by using the button bellow

{btn('My projects', '/My_pojects.html',)}""")

b(f"""## Contact Information
{img('discord-white.png', style={"margin-top": "20px", "margin-bottom": "20px",  "width": "32px", "height": "auto"}, link=True)}        afterhoursbilly#1234
{img('mail.png', style={"width": "42px", "height": "auto"}, link=True)} afterhoursbilly@gmail.com""", "content-block")
