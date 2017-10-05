---
layout: default
title: Aircraft & Environment
categories: [menu, content]
permalink: /mypages/aircraft-environment/
---

# The Aircraft and its Environment

This part introduces, although in simple terms, the concept aircraft as a _model_.
Some standard reference systems, and the nomenclature of the aircraft will be introduced,
as well as the significant forces, moments and angles affecting the atmospheric flight.

The aircraft operates in the atmosphere, therefore the standard air
model is reviewed, along with relevant approximating functions for performance
calculations. Some atmospheric effects in non-standard conditions are briefly
reviewed.

# Dynamic aviation

Every aeronautical vehicle or device producing a lift or thrust force accelerates
an amount of surrounding air in a downward and/or backward direction
by exerting a force in that direction on it. According to Newton's third law
of motion (*action = reaction*), the aircraft experiences an equal opposite
force, called lift $L$ or thrust $T$. If lift, for instance, which is typically
directed upwards, has the same magnitude as the aircraft weight $W$, an equilibrium
of forces, $W = L$, can be acquired for steady flight. A steady flight with a constant speed
is reached when also the aerodynamic resistance $D$ at that speed, opposite to
the flight direction, is equal to the produced thrust, $T = D$.

Conventional aircraft obtain their lift from a fixed lifting surface or aerofoil.
If this is greater or smaller than the weight or inclined sideways, the direction of
motion can be changed, making the aircraft manoeuvrable. Therefore, dynamic
aviation encompasses the essential condition that there must be a
continuous, downward flow of air around the aircraft.

# Misc images

{% include image.html
  url="/assets/img/ac_sideview_climb_forces.png"
  width="60%"
  description="Aircraft model in the vertical plane, with forces concentrated at the CoG."
  %}

{% include image.html
  url="/assets/img/ac_aerobatic_pull.png"
  width="100%"
  description="Aircraft CoG trajectory in a pull-up maneuver."
  %}

The atmospheric temperature...

{% include image.html
  url="/assets/img/T_h_ISA.png"
  width="90%"
  description="Air temperature variation with altitude according to the
    International Standard Atmosphere (ISA) model."
  %}
