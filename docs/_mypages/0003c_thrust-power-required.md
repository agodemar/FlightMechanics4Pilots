---
layout: default
title: Thrust and Power Required
categories: [menu, content, performance, thrust-power-required]
permalink: /mypages/thrust-power-required/
---

# Thrust and Power Required in Level Flight

<p><a href="{{ site.url }}/assets/Polari_Tecniche.pdf">Slides in Italian here.</a></p>

## Drag Polar Characteristic Points

{% include image.html
  url="/assets/img/Drag_Polar_Points_EPA.svg"
  width="80%"
  description="Characteristic points 'E', 'P', and 'A' on the parabolic drag polar. The point 'S' is taken on the actual drag polar."
  %}

## Thrust Technical Polar

{% include image.html
  url="/assets/img/ac_sideview_horizontal_simplified.png"
  width="80%"
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
T=D \quad \Longrightarrow \quad T \equiv T_\mathrm{R} \quad \Longrightarrow \quad C_D = \frac{T_\mathrm{R}}{\frac{1}{2}\rho V^2 S}
\label{eq:Performance:CD:T}
$$

$$
\frac{T_\mathrm{R}}{W} = \frac{D}{L} = \frac{1}{C_L/C_D} = \frac{1}{E}
  \quad \Longrightarrow \quad T_\mathrm{R} = \frac{W}{E}
\label{eq:Performance:T:Over:W}
$$

- $T_\mathrm{R}$ is the thrust required to fly at a given velocity in level, unaccelerated flight.
- Notice that minimum $T_\mathrm{R}$ is when airplane is flying at maximum $E$, i.e. at maximum $L/D$.
- $E=L/D$, aircraft aerodynamic efficiency is an important aero-performance quantity.
- $T_\mathrm{R}$ for airplane at given altitude varies with velocity.

{% include image.html
  url="/assets/img/Thrust_Required_Stall_Speed.svg"
  width="50%"
  description="Thrust technical polar. Example of thrust required for horizontal unaccelerated flight at a given altitude."
  %}

Example of required thrust calculation, for given aircraft weight $W$ and flight altitude $h$:

1. Select a flight speed $V$.
2. Calculate $C_L = W / \big( \frac{1}{2}\rho V^2 S \big)$.
3. Calculate $C_D$ from the polar: $$C_D = C_{D0} + C_L^2/\big( \pi \mathrm{A\!R} \, e \big)$$.
4. Calculate the efficiency $E = C_L/C_D$.
5. Calculate $T_\mathrm{R} = W/E$.

$T_\mathrm{R}$ is is how much thrust engine must produce to fly at selected speed -- at the given altitude
and at the given aircraft weight. It coincides with the amount of drag at the selected flight conditions.

The speed in level flight at the value $C_L$ of the lift coefficient is expressed as follows:

$$
V = \sqrt{\frac{2}{\rho}\strut} \, \sqrt{\frac{W}{S}\strut} \sqrt{\frac{1}{C_L}\strut}
  = \sqrt{\frac{2}{\rho_\mathrm{SL}\,\sigma(h)}\strut} \, \sqrt{\frac{W}{S}\strut} \sqrt{\frac{1}{C_L}\strut}
\label{eq:Level:Flight:Speed}
$$

That is, in level flight

$$
V \propto \frac{1}{\sqrt{C_L}} \quad \Leftrightarrow \quad C_L \propto \frac{1}{V^2}
\label{eq:Level:Flight:Speed:CL:Proportional}
$$

{% include image.html
  url="/assets/img/Level_Flight_V_CL.svg"
  width="60%"
  description="Airspeed in level flight and dependency on $C_L$ as well as angle of attack $\alpha$."
  %}

## Stall Speed

The minimum possible airspeed in level flight for given weight $W$ and flight altitude $h$:

$$
V_\mathrm{s} = \sqrt{\frac{2}{\rho}\strut} \, \sqrt{\frac{W}{S}\strut} \sqrt{\frac{1}{C_{L\mspace{2mu}\mathrm{max}}}\strut}
  = \sqrt{\frac{2}{\rho_\mathrm{SL}\,\sigma(h)}\strut} \, \sqrt{\frac{W}{S}\strut} \sqrt{\frac{1}{C_{L\mspace{2mu}\mathrm{max}}}\strut}
\label{eq:Stall:Speed}
$$

The stall speed varies with altitude as follows:

$$
V_\mathrm{s} =
  \frac{1}{\sqrt{\sigma}} \, V_{\mathrm{s,}\mspace{2mu}\mathrm{SL}}
\label{eq:Stall:Speed:Altitude}
$$
