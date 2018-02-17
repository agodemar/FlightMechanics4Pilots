---
layout: default
title: Dynamic Aviation
categories: [menu, content]
permalink: /mypages/airspeeds/
---

# Airspeeds

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

Equivalent airspeed

$$
V_\mathrm{EAS} = \left\{ \frac{2\,\gamma}{\gamma - 1} \frac{p}{\rho_\mathrm{SL}} \left[ \left( 1 + \frac{p_0 - p}{p}\right)^\frac{\gamma - 1}{\gamma} - 1 \right]\right\}^\frac{1}{2}
\label{eq:Airpeeds:EAS}
$$
