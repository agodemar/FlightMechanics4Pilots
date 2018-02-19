---
layout: default
title: Basic Anatomy of Airplane Flight
categories: [menu, content, introduction, anatomy-flight]
permalink: /mypages/anatomy-flight/
---

# Anatomy of Airplane Flight

In this section we recall some essential definitions that are useful for the study of airplane flight mechanics.

## Aerodynamic Angles

The first figure introduces the two aerodynamic angles that generate the aerodynamic forces and moments acting on the
airplane. These angles are the aircraft *sideslip angle* $\beta$ and the aircraft (absolute) angle of attack $\alpha$.
The sideslip $\beta$ is the angle formed by the instantaneous CoG velocity vector $\boldsymbol{V}$ and its projection
onto the airplane's symmetry plane. The projection is the *aerodynamic axis* called $x_\mathrm{A}$, a baricentric axis,
and shown in the figure.

{% include image.html
  url="/assets/img/ac_aerodynamic_angles.png"
  width="85%"
  description="Aircraft aerodynamic angles in a generic non-symmetric flight."
  %}

If the pilot sees a relative wing velocity $\boldsymbol{V} _ {\infty} = -\boldsymbol{V}$ coming from the right then the sideslip $\beta$ is
positive by definition. If the relative wind is in the plane of symmetry, i.e. $\beta = 0$, the flight is an
*aerodynamically symmetric flight* and the direction of $\boldsymbol{V}$ coincides with the direction of $x_\mathrm{A}$.

The angle between axes $x_\mathrm{A}$ and $x_\mathrm{B}$ is the aircraft body-angle of attack $\alpha_\mathrm{B}$.
The angle $\alpha = \alpha_\mathrm{B} + \mu_x$ between $x_\mathrm{A}$ and the zero-lift line of the wing is the
*absolute angle of attack* $\alpha$. This angle is shown in the above figure.

The aerodynamic axis $z_\mathrm{A}$ is taken, by construction, in the aircraft symmetry plane and positively oriented
as shown. The remaining aerodynamic axis $y_\mathrm{A}$ completes the frame and coincides with the bidy axis $y_\mathrm{B}$.

## Definitions of the Aircraft Lift and Drag

Next figure represents the simple case of an airplane in symmetric, wings level flight, with the CoG moving along a straight and horizontal
trajectory. By definition, the lift $L$ is such that $-L$ is the component of the resultant aerodynamic force
$$\boldsymbol{F}_\mathrm{A}$$ on the axis $z_\mathrm{A}$. The drag $D$ is so definad that $-D$ is the component of
$$\boldsymbol{F}_\mathrm{A}$$ along the axis $x_\mathrm{A}$.
In symmetric flight these are the only two components of $\boldsymbol{F}_\mathrm{A}$ and they are shown in the figure.

The flight condition considered below is such that the plane $x_\mathrm{A} y_\mathrm{A}$ is horizontal, that is, normal to
the local vertical direction given by the weight vector $\boldsymbol{W} = m \boldsymbol{g}$ passing through the CoG (point $G$).
The attitude of the fuselage is such that the body axis $x_\mathrm{B}$ forms an angle $\alpha_\mathrm{B}$ with respect to the
relative wind, being in this particular case the horizontal vector $-\boldsymbol{V}$.

horizontal plane. This angle is called *elevation angle* (sometimes erroneously also called 'pitch angle').
The above flight condition presents a horizontal velocity vector $\boldsymbol{V}$, i.e. a horizontal CoG trajectory, but an
inclined fuselage. This means that the angle $\theta$ coincides with the aerodynamic angle $\alpha_\mathrm{B}$.

{% include image.html
  url="/assets/img/ac_longitudinal_symmetric_four_forces.png"
  width="80%"
  description="Aircraft in wings level, horizontal flight. The typical ''Four Forces'' of symmetric flight are also shown."
  %}

## Climb Angle and Aircraft Elevation Angle (Fuselage Attitude)

A slightly different flight condition is represented below.

{% include image.html
  url="/assets/img/ac_longitudinal_symmetric.png"
  width="80%"
  description="Aircraft in wings level, climbing flight."
  %}

{% include image.html
  url="/assets/img/ac_climb_2.png"
  width="90%"
  description="Aircraft engaging a climb."
  %}

{% include image.html
  url="/assets/img/ac_climb_1.png"
  width="90%"
  description="Aircraft engaging a climb (sideview)."
  %}

## Thrust Orientation in Body-Axes

{% include image.html
  url="/assets/img/ac_sideview_thrust.png"
  width="90%"
  description="Thrust line of a propeller aircraft."
  %}

{% include image.html
  url="/assets/img/f16_engine_scheme.png"
  width="95%"
  description="Thrust line of a military jet aircraft."
  %}

## Wings Level Symmetric Flight

{% include image.html
  url="/assets/img/ac_sideview_climb_1.png"
  width="90%"
  description="Aircraft in wings level, climbing flight."
  %}
