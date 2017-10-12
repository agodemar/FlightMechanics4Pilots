---
layout: default
title: "isa"
tags:
    - python
    - notebook
categories: [menu, notebook]
---
# The International Standard Atmosphere (ISA)

We shall be concerned with altitudes below 31 km, or about 100000 ft.

**In [7]:**

{% highlight python %}
%run ./python/nb_init.py
%run ./python/isa.py
unit.load_definitions('./python/pint_addons.txt') # includes slug
{% endhighlight %}

**In [8]:**

{% highlight python %}
altitude = 0.0 *unit.m # Sea Level
{% endhighlight %}

**In [9]:**

{% highlight python %}
temperature, soundspeed, pressure, density = isa(altitude)
{% endhighlight %}

**In [10]:**

{% highlight python %}
print("Air properties at altitude h = {!s}".format(altitude))
print(" T = {:.6P}\n a = {:.5P}\n p = {:.4P}\n rho = {:.4fP}".format(temperature, soundspeed, pressure, density))
{% endhighlight %}

    Air properties at altitude h = 0.0 meter
     T = 288.15 kelvin
     a = 340.26 meter/second
     p = 1.013e+05 newton/meter²
     rho = 1.2252 kilogram·newton/joule/meter²


**In [16]:**

{% highlight python %}
print("Density in English units: {:.5P}".format(density.to(unit.slug/unit.ft**3)))
{% endhighlight %}

    Density in English units: 0.0023773 slug/foot³


**In [15]:**

{% highlight python %}
(1*unit.slug).to(unit.kilogram)
{% endhighlight %}




14.5939 kilogram


