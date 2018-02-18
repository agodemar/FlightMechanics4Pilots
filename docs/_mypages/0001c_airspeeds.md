---
layout: default
title: Airspeeds
categories: [menu, content, aircraft-environment, airspeeds]
permalink: /mypages/airspeeds/
---

# Airspeeds

## True Airspeed

The true airspeed $V$ of an aircraft is the speed of the aircraft relative to the airmass in which it is flying.
The true airspeed is commonly called TAS, or $V_\mathrm{TAS}$ (also KTAS, for knots true airspeed) and
it is important for accurate navigation of an aircraft.

TAS is not used for controlling the aircraft during taxiing, takeoff, climb, descent, approach or landing,
i.e. when the amount of power used and lift available are important to the various manoeuvers. For these purposes the
Indicated airspeed -- IAS or KIAS (knots indicated airspeed) -- is used.
However, since indicated airspeed only shows true speed through the air at standard sea level pressure and temperature,
a TAS meter is necessary for navigation purposes at cruising altitude in less dense air.

## Airspeed Measures

There is an aerodynamic instrument that actually measures the total pressure at a point in the flow: the *Pitot tube*.
The Pitot tube is utilized to measure the total combined pressures that are present when an aircraft moves through
the air. Static pressure, also known as ambient pressure, is always present whether an aircraft is moving or at rest.
It is simply the barometric pressure in the local area. Dynamic pressure, also called 'Q-bar' in aviation jargon,

$$
\bar{q} = \frac{1}{2} \rho V^2
$$

is present only when an aircraft is in motion; therefore, it can be thought of as a pressure due to motion.
The above definition of dynamic pressure remains the same for flows of all types, incompressible to hypersonic.

A scheme of a Pitot-satic system mounted on an aircraft is shown in the figure below.

{% include image.html
  url="/assets/img/Pitot_Static_System.png"
  width="90%"
  description="Pitot-static system and instruments."
  %}

A Pitot tube consists of a tube placed parallel to the flow and open to the flow at one end (point A).
The other end of the tube (point B) is closed. Now imagine that the flow is first started. Gas will
pile up inside the tube. After a few moments, there will be no motion inside the tube because the gas
has nowhere to go -- the gas will stagnate once steady-state conditions have been reached.
In fact, the gas will be stagnant everywhere inside the tube, including at point A.
As a result, the flow field sees the open end of the Pitot tube (point A) as an obstruction, and a
fluid element moving along the streamline, labeled C, has no choice but to stop when it arrives
at point A. Because no heat has been exchanged, and friction is negligible, this process will be
*isentropic*; that is, a fluid element moving along streamlines from C to A will be isentropically
brought to rest at point A by the very presence of the Pitot tube.
Therefore, the pressure at point A is, truly speaking, the *total pressure* $p_0$.
This pressure will be transmitted throughout the Pitot tube; and if a pressure gauge is placed at
point B, it will in actuality measure the total pressure of the flow.
In this fashion, a Pitot tube is an instrument that measures the total pressure of a flow.

By definition, any point of a flow where the speed is zero is called a *stagnation point*.
In the previous figure, point A is a stagnation point.

Consider the *static hole* D in the above figure. It is a small hole in the external surface of the
Pitot tube, called a *static pressure orifice*. Because the surface is parallel to the flow,
only the random motion of the gas molecules will be felt by the surface itself. In other words,
the surface pressure is indeed the static pressure $p$. This will be the pressure at the orifice
at point D. In contrast, the Pitot tube at point A will feel the total pressure $p_0$.
Normally the static pressure orifice at point D and the Pitot tube at point B are connected
across a pressure gauge, that will measure the difference between total and static pressure
$p_0 - p$.

The pressure difference $p_0 - p$ gives a measure of the flow velocity $V$.
A combination of a total pressure measurement and a static pressure measurement
allows us to measure the velocity at a given point in a flow. These two measurements can
be combined in the same instrument, a Pitot-static probe, as illustrated in the last figure.
A Pitot-static probe measures $p_0$ at the nose of the probe and $p$ at a point on the probe
surface downstream of the nose. The pressure difference $p_0 - p$ yields the velocity $V$,
but the quantitative formulation differs depending on whether the flow is low speed (incompressible),
high-speed subsonic, or supersonic.

### Incompressible subsonic formulation

At point D, i.e. at one of the static holes of the Pitot tube, the pressure is $p$ and
the velocity is $V$ (supervelocities due to the shape of the external shape of the tube are neglectable).
At point A, the pressure is $p_0$ and the velocity is zero. Applying Bernoulli's equation at points A and D,
we obtain

$$
p_0 = p + \frac{1}{2}\rho \, V^2
\label{eq:Airpeeds:Bernoulli}
$$

that is, the difference in static pressure between the points A and D is the dynamic pressure at
point D. The last relation *holds for incompressible flows only*. The total pressure equals the
sum of the static and the dynamic pressure. This yields the desired relation between $V$ and the
difference $p_0 - p$:

$$
\color{red}{ V = \sqrt{ \mathstrut 2\, \frac{p_0 - p}{\rho}} }
\label{eq:Airpeeds:V:Incompressible}
$$

In the incompressible regime where the density $\rho$ is a known constant value, the above formula
allows the calculation of flow velocity from a measurement of $p_0 - p$, obtained from a Pitot-static tube.
The constant density $\rho$ value can be obtained by measuring $p$ and $T$ and applying the
equation of state to calculate $\rho = p/(R\,T)$.

{% include image.html
  url="/assets/img/pitot-underwing.jpg"
  width="60%"
  description="Pitot tube mounted on a wing."
  %}

{% include image.html
  url="/assets/img/pitot-tubes-airliner.jpg"
  width="90%"
  description="Pitot probes on the fuselage nose of an airliner."
  %}

Either Pitot tubes or a Pitot-static tubes are used to measure the airspeed
of airplanes. Such tubes can be seen extending from airplane wing tips, with
the tube oriented in the flight direction, or from nose of fuselages.

If a Pitot tube by itself is used instead of a Pitot-static tube, then the ambient
static pressure in the atmosphere around the airplane is obtained from a static pressure
orifice placed strategically on the airplane surface. It is placed where the surface
pressure is nearly the same as the pressure of the surrounding atmosphere. Such a
location is found by experience. It is generally on the fuselage somewhere between
the nose and the wing.

{% include image.html
  url="/assets/img/pitot-f16.jpg"
  width="90%"
  description="Pitot probe on a military combat aircraft."
  %}

### Compressible subsonic formulation

Equation of state of air as a *perfect gas*

$$
p = \rho \, R \, T
\label{eq:Airpeeds:rhoRT}
$$

$$
c_p \, T = \frac{a^2}{\gamma - 1} = \frac{\gamma}{\gamma - 1} \frac{p}{\rho}
\label{eq:Airpeeds:cpT}
$$

- $c_p$, air isobaric specific heat
- $\gamma = 1.4$, air specific heat ratio

Equation of conservation of total energy

$$
 c_p \, T + \frac{1}{2} V^2 = c_p \, T_0
\label{eq:Airpeeds:Energy:A}
$$

- $T_0$, stagnation temperature

$$
 T_0 = T \left( 1 + \frac{V^2}{2\,c_p \, T} \right)
\label{eq:Airpeeds:Energy:B}
$$

For an isentropic flow

$$
 p_0 = p \left( \frac{T}{T_0} \right)^\frac{\gamma - 1}{\gamma}
\label{eq:Airpeeds:Isentropic:Flow}
$$

- $p_0$, stagnation pressure

True airspeed

$$
V_\mathrm{TAS} = V = \left\{ 2\, c_p \, T \left[ \left( 1 + \frac{p_0 - p}{p}\right)^\frac{\gamma - 1}{\gamma} - 1 \right]\right\}^\frac{1}{2}
\label{eq:Airpeeds:TAS:A}
$$

$$
V_\mathrm{TAS} = \left\{ \frac{2\, a^2}{\gamma - 1} \left[ \left( 1 + \frac{p_0 - p}{p}\right)^\frac{\gamma - 1}{\gamma} - 1 \right]\right\}^\frac{1}{2}
\label{eq:Airpeeds:TAS:B}
$$

$$
V_\mathrm{TAS} = \left\{ \frac{2\,\gamma}{\gamma - 1} \frac{p}{\rho} \left[ \left( 1 + \frac{p_0 - p}{p}\right)^\frac{\gamma - 1}{\gamma} - 1 \right]\right\}^\frac{1}{2}
\label{eq:Airpeeds:TAS:C}
$$

Traditionally $V_\mathrm{TAS}$ is measured using an analogue TAS indicator, but as the Global Positioning System (GPS)
has become available for both military and civilian use, the importance of such analogue instruments has decreased.

{% include image.html
  url="/assets/img/True_airspeed_indicator-FAA.png"
  width="60%"
  description="A mechanical true airspeed indicator for an airplane. The pilot sets the pressure altitude and air temperature in the top window using the knob; the needle indicates true airspeed in the lower left window."
  %}

## Equivalent Airspeed

$$
V_\mathrm{EAS} = \left\{ \frac{2\,\gamma}{\gamma - 1} \frac{p}{\rho_\mathrm{SL}} \left[ \left( 1 + \frac{p_0 - p}{p}\right)^\frac{\gamma - 1}{\gamma} - 1 \right]\right\}^\frac{1}{2}
\label{eq:Airpeeds:EAS}
$$

Calibrated airspeed

$$
V_\mathrm{EAS} = \left\{ \frac{2\,\gamma}{\gamma - 1} \frac{p_\mathrm{SL}}{\rho_\mathrm{SL}} \left[ \left( 1 + \frac{\color{red}{p_0 - p}}{p_\mathrm{SL}}\right)^\frac{\gamma - 1}{\gamma} - 1 \right]\right\}^\frac{1}{2}
\label{eq:Airpeeds:CAS}
$$

Dynamic pressure equivalence

$$
\left( \frac{1}{2} \, \rho \, V^2 \right) _ \mathrm{@SL} = \left( \frac{1}{2} \, \rho \, V^2 \right) _ {\mathrm{@}h} \Rightarrow \frac{1}{2} \, \rho_\mathrm{SL} \, V_\mathrm{SL}^2 = \frac{1}{2} \, \rho(h) \, V(h)^2
\label{eq:Airpeeds:Qbar:Equivalence:A}
$$

$$
V_\mathrm{EAS} = V_\mathrm{SL} = V(h) \sqrt{\mathstrut \frac{\rho(h)}{\rho_\mathrm{SL}} } = V(h) \sqrt{\mathstrut \sigma(h)}
\label{eq:Airpeeds:Qbar:Equivalence:B}
$$

$$
V_\mathrm{EAS} = V(h) \color{red}{ \sqrt{\mathstrut \sigma(h)} }
\label{eq:Airpeeds:Qbar:Equivalence:C}
$$

$$
V_\mathrm{TAS} = V_\mathrm{EAS} \, \color{red}{ \frac{1}{\sqrt{\mathstrut \sigma}} }
\label{eq:Airpeeds:TAS:EAS}
$$

The equivalent airspeed *is the airspeed at sea level in the International Standard Atmosphere at which the dynamic
pressure is the same as the dynamic pressure at the true airspeed (TAS) and altitude at which the aircraft is flying*.

Equivalent airspeed (EAS) is the calibrated airspeed (CAS) corrected for the compressibility of air at a non-trivial
Mach number.
In low-speed flight, EAS is the speed which would be shown by an airspeed indicator with zero error.[3] It is useful for predicting aircraft handling, aerodynamic loads, stalling etc.
