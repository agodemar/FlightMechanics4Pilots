---
layout: default
title: Cruising Flight
categories: [menu, content, performance, cruise]
permalink: /mypages/cruise/
---

# Level Unaccelerated Flight -- Cruising Flight

{% include image.html
  url="/assets/img/ac_sideview_horizontal_simplified.png"
  width="90%"
  description="Aircraft in wings level flight on a rectilinear, horizontal trajectory."
  %}

$$
\left\{
  \begin{array}{l}
  T = D \\[2ex]
  L = W
  \end{array}\right.
\label{eq:T:D:L:W}
$$

$$
L=W \quad \Longrightarrow \quad C_L = \frac{W}{\frac{1}{2}\rho V^2 S}
\label{eq:Performance:CL:W}
$$

$$
T=D \quad \Longrightarrow \quad C_D = \frac{T_\mathrm{R}}{\frac{1}{2}\rho V^2 S}
\label{eq:Performance:CD:T}
$$

$$
\frac{T_\mathrm{R}}{W} = \frac{D}{L} = \frac{1}{C_L/C_D} = \frac{1}{E}
\label{eq:Performance:T:Over:W}
$$

- $T_\mathrm{R}$ is thrust required to fly at a given velocity in level, unaccelerated flight.
- Notice that minimum $T_\mathrm{R}$ is when airplane is at maximum $L/D$.
- $E=L/D$, aircraft aerodynamic efficiency is an important aero-performance quantity.
- $T_\mathrm{R}$ for airplane at given altitude varies with velocity.

{% include image.html
  url="/assets/img/Thrust_Required.png"
  width="90%"
  description="Thrust required for horizontal unaccelerated flight at a given altitude."
  %}

Example of required thrust calculation:

1. Select a flight speed $V$.
2. Calculate $C_L = W / \big( \frac{1}{2}\rho V^2 S \big)$.
3. Calculate $C_D$ from the polar: $$C_D = C_{D0} + C_L^2/\big( \pi \mathrm{A\!R} \, e \big)$$.
4. Calculate the efficiency $E = C_L/C_D$.
5. Calculate $T_\mathrm{R} = W/E$.

$T_\mathrm{R}$ is is how much thrust engine must produce to fly at selected speed -- at the given altitude
and at the given aircraft weight.

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
