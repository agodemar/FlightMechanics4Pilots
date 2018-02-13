---
layout: default
title: The Atmosphere
categories: [menu, content]
permalink: /mypages/international-standard-atmosphere/
---

# The International Standard Atmosphere (ISA)

The knowledge of standard atmosphere is required for producing pressure instruments,
performing data reductions of flight tests, and pronouncing certain safety regulations
for the aircraft.

The physical characteristics of the atmosphere are not steady and constant but
change with altitude, location (longitude and latitude) on the globe, season, and
time of the day, and with the solar sunspot activity. The performance of an
aircraft depends on the physical characteristics of the atmospheric air through
which it flies. The performance data of an aircraft or comparison of the performance
of different aircraft have meaning only if they are considered with respect to
some commonly agreed upon *reference atmosphere*. This reference atmosphere
is usually the standard atmosphere, where the temperature, pressure, and
density vary with altitude only. The fixation of standard atmosphere allows for the
design of instruments for measuring altitude and airspeed. The pressure altitude,
temperature altitude, and density altitude have meaning only after the standard
atmosphere has been specified.

It is presently possible to specify the prevailing atmospheric conditions up to
an altitude of 2000 km at any latitude and longitude of our globe. If desired,
each country can have its own standard atmosphere. For general aviation purposes
it is pertinent to develop internationally known reference atmosphere. Several
reference atmospheric models have been established.

A number of standard versions exist: NACA's atmosphere (1955), the ARDC (1959),
the US standard (1962, amended in 1976) and the ICAO standard.
These tables are basically equivalent to each other up to about 20 km (65000 ft),
that covers most of the atmospheric flight mechanics.
We shall be concerned with altitudes below 31&nbsp;km, or about 100000&nbsp;ft.

## The ISA Thermodynamic model

Air temperature distribution is the most important element of the atmosphere as
it also controls the other elements of the atmosphere. In a standard atmosphere, the
temperature distribution is obtained by making several measurements at different
altitudes. The temperature distribution of the U.S. standard atmosphere 1976, is
presented in the figure below up to an altitude of 110&nbsp;km.

{% include image.html
  url="/assets/img/ISA_Temperature.png"
  width="80%"
  description="Air temperature variation with altitude according to the
    International Standard Atmosphere (ISA) model."
  %}

Next figure reports the ISA temperature up to 16&nbsp;km with to variation of the
model better suited for tropical and artic latitudes.

{% include image.html
  url="/assets/img/T_h_ISA.png"
  width="90%"
  description="Air temperature variation with altitude according to the
    International Standard Atmosphere (ISA) model."
  %}


The temperature distribution in the standard atmosphere consists of mostly straight lines.
Thus, the atmosphere has either isothermal regions of zero lapse rate, or constant gradient
regions of positive or negative lapse rates. The lapse rate is positive in troposphere
and mesosphere. The isothermal regions in the above figures are: 1) from 11.1&nbsp;km to 20 km,
2) from 47.4&nbsp;km to 51&nbsp;km, and 3) from 86&nbsp;km to 91&nbsp;km.
The lapse rates

\begin{equation}
\lambda = - \mathrm{d}T / \mathrm{d}h
\label{eq:ISA:Lapse:Rate}
\end{equation}

in different regions can be calculated.

Having obtained the temperature variation empirically, the pressure and density
variations are calculated from the hydrostatic relation and the equation of state
by assuming that the medium of air is continuum, perfect gas, and at rest. It will
be shown here that the variations of pressure and density with altitude can be
expressed analytically.

By the perfect gas hypothesis

\begin{equation}
p = \rho \, R\, T
\label{eq:Air:Perfect:Gas}
\end{equation}
where $p$, $\rho$, and $T$ are the local pressure, density and temperature, it can be shown
that a small change in altitude $\mathrm{d}h$ determinse a change in pressure $\mathrm{d}p$
such that

\begin{equation}
\frac{\mathrm{d}p}{p} = - g_0 \, \frac{\mathrm{d}h}{RT}
\label{eq:Air:Stevino:Pressure}
\end{equation}

where $g_0$ is the constant gravity acceleration. The above equation is kknown as the *law of Stevino*.
From the definition of lapse rate the above equation yields

\begin{equation}
\frac{\mathrm{d}p}{p} = g_0 \, \frac{\mathrm{d}h}{\lambda R T}
\label{eq:Air:Stevino:Temperature}
\end{equation}

The ISA values at sea level (SL) of the air density, pressure and speed of sound are the following:

- $\rho_\mathrm{SL} = 1.225\,\mathrm{kg}/\mathrm{m}^3$
- $T_\mathrm{SL} = 15.15\,{}^\circ\mathrm{C} = 288.15\,{}^\circ\mathrm{K}$
- $a_\mathrm{SL} = 340.294\,\mathrm{m/s}$
- $g_0 = 9.807\,\mathrm{m/s}^2$

The following nondimensional ratios are introduced:
\begin{equation}
\sigma = \frac{\rho}{\rho_\mathrm{SL}}\,,\;\;
\delta = \frac{p}{p_\mathrm{SL}}\,,\;\;
\Theta = \frac{T}{T_\mathrm{SL}}\,,\;\;
\bar{a} = \frac{a}{a_\mathrm{SL}}
\label{eq:ISA:Ratios}
\end{equation}

which are plotted below

{% include image.html
  url="/assets/img/ISA_ratios.png"
  width="80%"
  description="Variations of ratios $\sigma$, $\delta$, $\Theta$, and $\bar{a}$ with altitude according
    International Standard Atmosphere (ISA) model."
  %}
