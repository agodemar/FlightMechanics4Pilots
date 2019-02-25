---
layout: default
title: Level Flight Performance
categories: [menu, content, performance, level-flight]
permalink: /mypages/level-flight/
---

# Level Unaccelerated Flight Performance

<p><a href="{{ site.url }}/assets/Volo_Livellato.pdf">Slides in Italian here.</a></p>

{% include image.html
  url="/assets/img/Thrust_Requirement.png"
  width="90%"
  description="Different points on the $T_\mathrm{R}$ curve correspond to different angles of attack."
  %}

The thrust required for horizontal flight must compensate the different formas of drag, i.e.

- The *parassitic drag*, varying with $\bar{q} \sim V^2$.
- The *induced drag*, varying with $1/\bar{q} \sim 1/V^2$.


{% include image.html
  url="/assets/img/Parassitic_Vs_Induced_Drag.png"
  width="90%"
  description="Parassitic versus induced drag."
  %}

It can be proved analytically that, assuming a parabolic drag polar, the condition for flight at
 minimum $T_\mathrm{R}$ occurs when the the aircraft develops a drag coefficient whose value is given by the
 two equal halves: $C_{D0} = C_{D\mathrm{i}}$.

{% include image.html
  url="/assets/img/TR_Minimum.png"
  width="90%"
  description="Condition of minimum thrust required."
  %}

{% include image.html
  url="/assets/img/TR_Maximum_V.png"
  width="90%"
  description="Condition of minimum thrust required."
  %}
