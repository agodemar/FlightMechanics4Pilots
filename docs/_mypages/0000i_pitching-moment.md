---
layout: default
title: Pitching Moment
categories: [menu, content, intro, pitching-moment]
permalink: /mypages/pitching-moment/
---

# Aerodynamic Pitching Moment

## Center of Pressure (CP)

The aerodynamic interaction of a wing with an airflow determines a distribution of
varying local pressures and tangential stresses on the external surface. This is also called the *wet surface* of the wing.
The same concept applies to all remaining parts of an aircraft that are exposed to the flow, such as the external shape of the fuselage
as well as the wet surfaces of tailplanes.

The local pressures and tangential stresses, provided they are multiplied by the area $\mathrm{d}\mathcal{A}$ of the elemental wet surface,
represent a *system of applied forces*. In general, these forces are non-coplanar and non-parallel yet they can be resolved into an *equivalent single force*
represented by the resultant, applied along a well determined axis. The aerodynamic resultant $\mathbf{F}$ is a representative force which has the same physical effect on a given
body, in our case the aircraft, as the group of forces it replaces. In aerodynamics this conceptual process is known as *reduction* of the overall aerodynamic
action of the airflow on the airplane *to the resultant aerodynamic force*, applied to *center of pressure*. Actually, the resultant can be applied to any given
point of its line of action.

When airfoils are considered, the aerodynamic resultant is a force per unit span $\mathbf{f}$, which is applied on a point
on the chord, i.e. the center of pressure of airfoils is represented on the chord. This is illustrated by the next figure.
The vectors $\mathbf{n}$ are the local unit vector normal to the airfoil and pressure difference vectors $(p-p_\infty)\mathbf{n}$ represent the
local normal strain exerted on the airfoil external shape by the flow. These vectors, multiplied by the small areas $\mathrm{d}\mathcal{A} = \mathrm{d}s\cdot 1\,\mathrm{m}$
(where $\mathrm{d}s$ is the element of curvilinear abscissa running along the airfoil and $1\,\mathrm{m}$ is the unit spanwise length) are forces
distributed on the external surface of the airfoil. A symilar system of vector exists and is represented by the vectors
$\tau_\mathrm{w}\mathbf{t}$, where $\tau_\mathrm{w}$ are the local viscous tangential stresses and $\mathbf{t}$ are the local unit vectors tangent
to the airfoil. The ensemble of all these force vectors applied on the airfoil contour give rise to the the resultant $\mathbf{f}$ shown below.

{% include image.html
  url="/assets/img/Airfoil_Pressures_Reduction.png"
  width="70%"
  description="Reduction of pressure distribution over the airfoil external surface to the aerodynamic resultant force $f$ applied to the center of pressure (CP)."
  %}

The system of all local external forces on the airfoil, due to the airflow of asymptotic speed $V_\infty$ at an angle of attack $\alpha$,
is equivalent to the resultant $\mathbf{f}$, which is *reduced* to the center of pressure $\mathrm{CP}$. Therefore, to the point $\mathrm{CP}$
are applied both the lift per unit span $\ell$ and the drag per unit span $d$.

The same is done for finite wings for which the center of pressure is taken on the root chord, i.e. the resultant $\mathbf{F}_\mathrm{W}$ acts in the plane of symmetry.

{% include image.html
  url="/assets/img/Wing_Alpha_Pressure_Reduction.png"
  width="100%"
  description="External aerodynamic actions on a wing reduced the aerodynamic resultant force $F_\mathrm{W}$ applied to the center of pressure (CP) on the root chord."
  %}

Due to the high values of aerodinamic efficiencies of airfoils and wings, often one can *neglect the drag component* in the above constructions,
i.e. $d\approx 0$ and $L_\mathrm{W}\approx 0$.

## Aerodynamic Center

The figure below represents an airfoil at a given angle of attack $\alpha$, developing a lift $\ell$ reduced to the center of pressure.
It is known from the aerodynamics that, for a fixed airspeed $V_\infty$, an *increasing angle of attack* determines an increase of $\ell$
and a movement of the point $\mathrm{CP}$ along the chord *towards the leading edge*. This forward shift takes place until $\alpha$ reaches the stall angle
of attack $\alpha_\mathrm{stall}$ of the airfoil when, for a further increase of $\alpha$, the center of pressure
starts shifting backwards.

{% include image.html
  url="/assets/img/Airfoil_Pressures_Reduction_Simplified.png"
  width="70%"
  description="Approximated reduction of airfoil pressure distribution to the lift $\ell$ to the center of pressure (CP)."
  %}

{% include image.html
  url="/assets/img/Airfoil_Cmc4_Vs_alpha_curve.png"
  width="60%"
  description="Airfoil pitching moment coefficient with respect to a pole at the quarter-chord versus angle of attack."
  %}

{% include image.html
  url="/assets/img/Airfoil_Center_Pressure.png"
  width="90%"
  description="Airfoil center of pressure (CP) variation with angle of attack. System reduction to the aerodynamic center at $c/4$ (approximately)."
  %}

{% include image.html
  url="/assets/img/Wing_Topview_Aerodynamic_Center.png"
  width="80%"
  description="Wing top view showing the mean aerodynamic chord $\bar{c}$ and the wing aerodynamic center."
  %}

{% include image.html
  url="/assets/img/Wing_Cmac_Vs_alpha_curve.png"
  width="60%"
  description="Wing pitching moment coefficient with respect to aerodynamic center versus angle of attack."
  %}

{% include image.html
  url="/assets/img/B747_fuselage_topview_2_en.png"
  width="100%"
  description="Boeing 747 wing-fuselage configuration. Aerodynamic center of the isolated wing and of the wing-body combination."
  %}

{% include image.html
  url="/assets/img/B747_fuselage_sideview_1.png"
  width="100%"
  description="Boeing 747 fuselage side view."
  %}

{% include image.html
  url="/assets/img/B747_fuselage_Cm_vs_alpha.png"
  width="100%"
  description="Boeing 747 fuselage pitching moment. The effect of the wing presence is included."
  %}
