---
layout: default
title: Types of Aircraft
categories: [menu, content, introduction]
permalink: /mypages/anatomy-conventional-aircraft/
---

# The Anatomy of Conventional Aircraft Configurations

This section introduces a set of definitions pertaining the architecture of conventional fixed-wing airplanes, which are useful in the discussion of aircraft performance characteristics. Since pilots already possess a knowledge of aircraft fundamentals by training, the concepts introduced here are more oriented towards and flight theory.

## Aircraft Body Axes

The figure below represents a conventional three-axis architecture aircraft and a reference frame $$\{ G, x, y, z \}$$ fixed with vehicle.

{% include image.html
  url="/assets/img/ac_body_axes.png"
  width="80%"
  description="Aircraft body-fixed reference frame, with origin at CoG."
  %}

The above cartesian reference is called *body-frame*, having the origin at the aircraft center of gravity (CoG) $G$ and the three oriented as shown. For this reason the *body-axes* are also named $x_\mathrm{B}$, $y_\mathrm{B}$, and $z_\mathrm{B}$.

## Planform definitions

The figure below shows a top view af an aircraft.

{% include image.html
  url="/assets/img/ac_topview.png"
  width="60%"
  description="Aircraft top view. Wing span $b=2s$."
  %}

Two of the quantities that characterize the wing planform are also shown:

- $b=2s$, wing span;
- $\bar{c}$, mean chord taken over all the chords $c(y)$ at wing sections $y$ for $-\frac{b}{2} \le y \le +\frac{b}{2}$.

{% include image.html
  url="/assets/img/wing_basic.png"
  width="80%"
  description="A wing and its profiles (sections)."
  %}

## Wing-Fuselage definitions

A more detailed nomenclature is given by the next drawing, representing a top and a side view of a wing-fuselage combination.

{% include image.html
  url="/assets/img/ac_wing_fuselage_definitions_1.png"
  width="70%"
  description="Nomenclature of wing-fuselage combination (side view)."
  %}

The axes $x_\mathrm{C}$, $y_\mathrm{C}$, and $z_\mathrm{C}$ are what designers call *construction axes*. Like the body-axes, also the construction axes are fixed with the aircraft but are oriented differently. In the above illustration the various quantities are used to identify the position of the wing relative to the fuselage body. Typically, the body and construction axes $x_\mathrm{B}$ and $x_\mathrm{C}$ are parallel, but the latter is not baricentric and passes through the fuselage nose.

The quantities represented above have the following significance:

- $l_\mathrm{B}$, fuselage length;
- $b_\mathrm{B}$, $h_\mathrm{B}$, maximum fuselage width and fuselage height;
- $A$, wing apex point, i.e. leading edge of wing root when wing leading edge line is ideally extended up to the symmetry plane;
- $A^\star$, leading edge of the effective wing root, i.e. of the attachment profile at the wing-fuselage junction;
- $c_{\mathrm{r}}^\star$, chord of the effective wing root;
- $i_{\mathrm{W}}^\star$, wing incidence or wing *rigging angle*, i.e. a mounting angle formed by the wing root chord and the fuselage reference line $x_\mathrm{C}$.

The next figures shows a front view the wing-fuselage combination.

{% include image.html
  url="/assets/img/ac_wing_fuselage_definitions_2.png"
  width="75%"
  description="Nomenclature of wing-fuselage combination (front view)."
  %}

Two more quantities are introduced:
- $\Gamma$, the wing dihedral angle;
- $z_0$, the vertical position of the wing with respect to the fuselage reference line $y_\mathrm{C}$.


## The Zero-Lift direction of a Wing  

An important angle, related to the lift capacity of the wing of a given aircraft, is shown in the next figure.

{% include image.html
  url="/assets/img/ac_sideview_mu_x.png"
  width="70%"
  description="Aircraft side view and wing zero-lift line."
  %}

The angle $\mu_x$ is that formed by the wing zero-lift direction with the longitudinal body axis $x_\mathrm{B}$.

## Fuselage definitions

{% include image.html
  url="/assets/img/fuselage_isoview_c172.png"
  width="70%"
  description="Nomenclature of the fuselage."
  %}

## The Horizontal Tailplane

{% include image.html
  url="/assets/img/wing_fuselage_htail_definitions_1.png"
  width="70%"
  description="Nomenclature of the horizontal tailplane."
  %}

{% include image.html
  url="/assets/img/fuselage_isoview_c172_Htail.png"
  width="70%"
  description="Nomenclature of the horizontal tailplane."
  %}

{% include image.html
  url="/assets/img/htail_planform.png"
  width="70%"
  description="Horizontal tailplane planform."
  %}

{% include image.html
  url="/assets/img/horizontal_tail_profile.png"
  width="50%"
  description="Horizontal tailplane section."
  %}

{% include image.html
  url="/assets/img/horizontal_tail_profile_deltaE.png"
  width="50%"
  description="Elevator deflection."
  %}

{% include image.html
  url="/assets/img/horizontal_tail_profile_deltaE_deltaT.png"
  width="50%"
  description="Elevator and trim tab combined deflections."
  %}

## The Vertical Tailplane

{% include image.html
  url="/assets/img/fuselage_isoview_c172_Vtail.png"
  width="80%"
  description="Nomenclature of the vertical tailplane."
  %}

{% include image.html
  url="/assets/img/ac_rudder_control.png"
  width="80%"
  description="Rudder deflection."
  %}

## Conventional Flight Controls

{% include image.html
  url="/assets/img/aerosurface_command_line.png"
  width="70%"
  description="Flight controls."
  %}

{% include image.html
  url="/assets/img/ac_aerosurface_deflections.png"
  width="100%"
  description="Positive deflection angles of conventional aircraft control surfaces."
  %}
