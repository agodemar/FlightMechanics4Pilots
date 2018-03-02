---
layout: default
title: Aircraft Drag Polar
categories: [menu, content, performance, drag-polar]
permalink: /mypages/drag-polar/
---

# Aircraft Drag Polar

<p><a href="{{ site.url }}/assets/Polare_di_resistenza.pdf">Slides in Italian here.</a></p>

## Aircraft parabolic drag polar

$$
C_D = C_{D0} + K\,C_L^2
\label{eq:Drag:Polar:Parabolic:A}
$$

$$
K = \frac{1}{\pi\, \mathrm{A\!R} \, e}
\label{eq:K:Drag:Polar:Parabolic}
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

Actual polar:

{% include image.html
  url="/assets/img/Drag_Polar_Actual.svg"
  width="50%"
  description="Aircraft parabolic and actual drag polar."
  %}

## Generalized parabolic polar

$$
C_D = C_{D\mspace{2mu}\mathrm{min}} + K\,\left( C_L - C_{L\mspace{2mu}\mathrm{ideal}} \right)^2
\label{eq:Drag:Polar:Parabolic:B}
$$

- $C_{L\mspace{2mu}\mathrm{ideal}} = C_L @ C_{D\mspace{2mu} \mathrm{min}}$, ideal lift coefficient, i.e. $C_L$ at the angle of attack
  of minimum $C_D$.

Equation (\ref{eq:Drag:Polar:Parabolic:B}) is unnecessarily too complicated. An acceptable approximation is given by
the simple parabolic drag polar (\ref{eq:Drag:Polar:Parabolic:A}).

{% include image.html
  url="/assets/img/Drag_Polar_CL_ranges.svg"
  width="70%"
  description="Validity of aircraf parabolic drag polar for normal operative conditions."
  %}

## Equivalent parassite area

$$
f = C_{D0} \, S
\label{eq:f:Parassite:Equivalent:Area}
$$

$$
f = C_{f\mspace{2mu}\mathrm{e}} \, S_\mathrm{wet}
\label{eq:f:Parassite:Equivalent:Area:Swet}
$$

$$
f = C_{f\mspace{2mu}\mathrm{e}} \, S_\mathrm{wet} \quad \Rightarrow \quad
C_{D0} = \frac{f}{S} \quad \Rightarrow \quad
C_{D0} = C_{f\mathrm{e}} \, \frac{S_\mathrm{wet}}{S}
\label{eq:CD0:f:Swet}
$$

$$
C_{f\mspace{2mu}\mathrm{e}} = 1.5 \cdot C_{f\mspace{2mu}\mathrm{turb}}
\label{eq:Cfe:Cfturb}
$$

- $C_{f\mspace{2mu}\mathrm{turb}}$, friction coefficient of a flat plate aligned with the flow,
  calculated in turbulent regime at the aircraft flight Reynolds number $\mathrm{Re} = \rho V \bar{c}/\mu$.

## Oswald efficiency factor

$$
e = f \left( M, \mathrm{A\!R}, \Lambda_\mathrm{le} \right)
\label{eq:e:Drag:Polar}
$$

(various calculation methods in literature)
