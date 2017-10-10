---
layout: default
title: "legend"
tags:
    - python
    - notebook
categories: [menu, notebook]
---
**In [1]:**

{% highlight python %}
%matplotlib inline
{% endhighlight %}


# Legend using pre-defined labels


Notice how the legend labels are defined with the plots!



**In [2]:**

{% highlight python %}
import numpy as np
import matplotlib.pyplot as plt

# Make some fake data.
a = b = np.arange(0, 3, .02)
c = np.exp(a)
d = c[::-1]

# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')

legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

plt.show()
{% endhighlight %}


![png]({{ site.url }}/mypages/legend_files/legend_2_0.png)

