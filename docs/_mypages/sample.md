---
layout: default
title: "sample"
tags:
    - python
    - notebook
categories: [menu, notebook]
---
# My sample Jupyter Notebook

**In [3]:**

{% highlight python %}
import sys
sys.version_info
{% endhighlight %}




    sys.version_info(major=3, minor=5, micro=4, releaselevel='final', serial=0)



**In [4]:**

{% highlight python %}
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
{% endhighlight %}

**In [5]:**

{% highlight python %}
x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp');
{% endhighlight %}


![png]({{ site.url }}/mypages/sample_files/sample_3_0.png)


## Setting up files for Jekyll

From the command line:
`jupyter nbconvert --to markdown <notebook>.ipynb --config jekyll.py`
