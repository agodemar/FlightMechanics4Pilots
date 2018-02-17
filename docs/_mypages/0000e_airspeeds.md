---
layout: default
title: Airspeeds
categories: [menu, content]
permalink: /mypages/airspeeds/
---

# Airspeeds

## True Airspeed

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
