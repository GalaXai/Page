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
  links:
    - icon: discord
      text: b1x4#9406
      href: https://www.discord.com/users/1063240042291671050
    - icon: github
      text: GitHub
      href: https://github.com/GalaxUniv
    - icon: twitter
      text: Twitter
      href: https://twitter.com/afterhoursbilly
    - icon: chevron-bar-left
      text: Kaggle
      href: https://www.kaggle.com/galaxqq
    - icon: envelope
      text: afterhoursbilly@gmail.com
      href: mailto:afterhoursbilly@gmail.com
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

Hello,I am aspiring Data Scientist and Software Enginer,I am currently in my second year Computer Science, currently exploring the fascinating field of Deep Learning. \n 
Although I may not have any commercial experience, I have been passionately delving into the intricacies of Deep Learning concepts and have created some small projects to demonstrate my skills. You can find most of my projects on my Github and Kaggle profile, or by visiting the Projects tab on this page, or by clicking the button bellow.

{btn('My projects', '/My_pojects.html',)}""")

b(f"""## Contact Information""", "content-block")
