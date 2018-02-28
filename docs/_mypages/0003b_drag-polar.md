---
layout: default
title: Basic Laws
categories: [menu, content, performance, drag-polar]
permalink: /mypages/drag-polar/
---

# Drag Polar

<p><a href="{{ site.url }}/assets/Polare_di_resistenza.pdf">Slides in Italian here.</a></p>

Aircraft parabolic drag polar:

$$
C_D = C_{D0} + K\,C_L^2
\label{eq:Drag:Polar}
$$

$$
K = \frac{1}{\pi\, \mathrm{A\!R} \, e}
\label{eq:K:Drag:Polar}
$$

- $C_{D0}$, parasite drag coefficient at zero lift.
- $$C_{D\mathrm{i}} = C_L^2/\big(\pi \mathrm{A\!R} \, e\big)$$, drag coefficient due to lift (induced drag).
- $e$, Oswald efficiency factor, includes all effects from airplane.
- $$\mathrm{A\!R}_\mathrm{e}=\mathrm{A\!R}\,e$$, effective aspect ratio.
- $b_\mathrm{e}=b\sqrt{e}$, effective wing span.

Parabolic polar:

{% include image.html
  url="/assets/img/Drag_Polar_Parabolic.svg"
  width="40%"
  description="Aircraft parabolic drag polar."
  %}

Real polar:

{% include image.html
  url="/assets/img/Drag_Polar_Real.svg"
  width="60%"
  description="Aircraft parabolic drag polar."
  %}
