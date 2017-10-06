---
layout: default
title: "sample"
tags:
    - python
    - notebook
categories: [menu, notebook]
---
# My sample Jupyter Notebook

**In [9]:**

{% highlight python %}
import sys
sys.version_info
{% endhighlight %}




    sys.version_info(major=3, minor=5, micro=4, releaselevel='final', serial=0)



**In [10]:**

{% highlight python %}
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
{% endhighlight %}

**In [11]:**

{% highlight python %}
x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp');
{% endhighlight %}


![png]({{ site.url }}/mypages/sample_files/sample_3_0.png)


## Setting up files for Jekyll

From the command line:
`jupyter nbconvert --to markdown <notebook>.ipynb --config jekyll.py`

Now some LaTeX magic:

$$
E = m c^2
$$

Be aware that this is a markdown cell inside a Jupyter notebook, and the formula
is converted by Jupyter.

## Experiments

**In [12]:**

{% highlight python %}
import math
import numpy as np
import tables as pt
from IPython.display import display, Math, Latex, SVG
{% endhighlight %}

### The wing

**In [13]:**

{% highlight python %}
c_r = 4.0; c_t = 1.5; b = 27; Lambda_le = 25*math.pi/180
{% endhighlight %}

**In [14]:**

{% highlight python %}
Latex(
    r'\begin{array}{rl}'
    +  r'\text{root chord,}\, c_{\mathrm{r}}: & ' + r'{0}'.format(c_r) + r'\,\text{m}'
    +  r'\newline'
    +  r'\text{tip chord,}\, c_{\mathrm{t}}: & ' + r'{0}'.format(c_t) + r'\,\text{m}'
    +  r'\newline'
    +  r'\text{span,}\, b: & ' + r'{0}'.format(b) + r'\,\text{m}'
    +  r'\newline'
    +  r'\text{leading edge sweep,}\, \Lambda_{\mathrm{le}}: &' 
    +    r'{0}'.format(Lambda_le*180/math.pi) + r'\,\text{deg}'
    +r'\end{array}'
)
{% endhighlight %}




\begin{array}{rl}\text{root chord,}\, c_{\mathrm{r}}: & 4.0\,\text{m}\newline\text{tip chord,}\, c_{\mathrm{t}}: & 1.5\,\text{m}\newline\text{span,}\, b: & 27\,\text{m}\newline\text{leading edge sweep,}\, \Lambda_{\mathrm{le}}: &25.0\,\text{deg}\end{array}


