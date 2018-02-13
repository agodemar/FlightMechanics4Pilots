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
of different aircraft *have meaning only* if they are considered with respect to
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
These models, available in tabular form, are basically equivalent to each other
up to about 20 km (65000&nbsp;ft), that covers most of the atmospheric flight mechanics.
We shall be concerned with altitudes below 31&nbsp;km, or about 100000&nbsp;ft.

## The ISA Thermodynamic model

Air temperature distribution with altitude is the most important characteristic as
it also determines the other elements of the atmosphere model. In a standard atmosphere, the
temperature distribution is obtained by making several measurements at different
altitudes. The temperature distribution of the U.S. standard atmosphere 1976, is
presented in the figure below up to an altitude of 105&nbsp;km.

{% include image.html
  url="/assets/img/ISA_Temperature.png"
  width="80%"
  description="Air temperature variation with altitude according to the
    International Standard Atmosphere (ISA) model."
  %}

Next figure reports the ISA temperature up to 16&nbsp;km with two variations of the
model better suited for tropical and artic latitudes.

{% include image.html
  url="/assets/img/T_h_ISA.png"
  width="90%"
  description="Air temperature variation with altitude according to the
    International Standard Atmosphere (ISA) model."
  %}


The temperature distribution in the standard atmosphere consists of mostly straight lines,
each one characterized by a constant lapse rate

\begin{equation}
\lambda = - \mathrm{d}T / \mathrm{d}h
\label{eq:ISA:Lapse:Rate}
\end{equation}

Thus, the atmosphere has either isothermal regions of zero lapse rate, or constant gradient
regions of positive or negative lapse rates. The lapse rate $\lambda$ is positive in troposphere
and mesosphere. The isothermal regions in the above figures are: 1) from 11.1&nbsp;km to 20 km,
2) from 47.4&nbsp;km to 51&nbsp;km, and 3) from 86&nbsp;km to 91&nbsp;km.

Having obtained the temperature variation empirically, the pressure and density
variations are calculated from the laws of hydrostatics and from the equation of state
by assuming that the medium of air is continuum, perfect gas, and at rest.
The variations of pressure and density with altitude can then be expressed analytically.

By the perfect gas hypothesis the local air pressure is given by the equation of state

\begin{equation}
p = \rho \, R\, T
\label{eq:Air:Perfect:Gas}
\end{equation}

where $\rho$ is the density, $T$ is the temperature, and
$R = 287\,\mathrm{J}/(\mathrm{kg}\,{}^\circ\mathrm{K})$ is the air constant.
Moreover, the local speed of sound $a$ is given by the equation

\begin{equation}
a = \big(\,\gamma \, R \, T \, \big)^{\frac{1}{2}}
\label{eq:Air:Perfect:Gas:Sound}
\end{equation}


where $\gamma = 1.4$ is the air specific heat ratio.

It can be shown that a small difference in altitude $\mathrm{d}h$ corresponds to a
vertical difference in static pressure $\mathrm{d}p$ such that

\begin{equation}
\frac{\mathrm{d}p}{p} = - g_0 \, \frac{\mathrm{d}h}{R \, T}
\label{eq:Air:Stevino:Pressure}
\end{equation}

where $g_0 = 9.807\,\mathrm{m/s}^2$ is the gravity acceleration at sea level (assumed constant
throughout the atmosphere).
The above equation is known as the *law of Stevino* that, combined with the definition of lapse rate,
yields

\begin{equation}
\frac{\mathrm{d}p}{p} = g_0 \, \frac{\mathrm{d}h}{\lambda \, R\, T}
\label{eq:Air:Stevino:Temperature}
\end{equation}

From the ISA values of air properties at sea level (SL)

- $\rho_\mathrm{SL} = 1.225\,\mathrm{kg}/\mathrm{m}^3$
- $p_\mathrm{SL} = 1.0133\cdot 10^5 \,\mathrm{N}/\mathrm{m}^2$
- $T_\mathrm{SL} = 15.15\,{}^\circ\mathrm{C} = 288.15\,{}^\circ\mathrm{K}$
- $a_\mathrm{SL} = 340.294\,\mathrm{m/s}$

the following nondimensional ratios are introduced:

\begin{equation}
\sigma = \frac{\rho}{\rho_\mathrm{SL}}\,,\;\;
\delta = \frac{p}{p_\mathrm{SL}}\,,\;\;
\Theta = \frac{T}{T_\mathrm{SL}}\,,\;\;
\bar{a} = \frac{a}{a_\mathrm{SL}}
\label{eq:ISA:Ratios}
\end{equation}

These are plotted in the next figure.

{% include image.html
  url="/assets/img/ISA_ratios.png"
  width="80%"
  description="Variations of ratios $\sigma$, $\delta$, $\Theta$, and $\bar{a}$ with altitude according
    International Standard Atmosphere (ISA) model."
  %}

In flight, when a value of the external pressure $p$ is known and the corresponding altitude is found
by entering the above figure with the ratio $p/p_\mathrm{SL}$ the resulting value is called
*pressure-altitude*. If the local temperature is known and the figure is entered with the ratio
$T/T_\mathrm{SL}$ then the resulting altitude is called *temperature-altitude*.
When the same process is based on a known density value then the resulting altitude is called
*density-altitude*.
For example, a pressure $p = 54019\,\mathrm{N}/\mathrm{m}^2$, i.e. a relative pressure
$\delta = 0.533$, yields a pressure-altitude of $5000\,\mathrm{m}$.

In the troposphere, where the temperature law is

\begin{equation}
T(h) = T_\mathrm{SL} - \lambda_\mathrm{tropo} \, h
\label{eq:ISA:Temperature:Troposphere}
\end{equation}

with $\lambda_\mathrm{tropo} = 0.0065\,{}^\circ\mathrm{C/m}$, given the SL values
reported above, it is easy to show that

\begin{equation}
\delta (h) = \left( \frac{T(h)}{T_\mathrm{SL}} \right)^{\frac{g_0}{\lambda R}}
  = \left( \frac{T(h)}{T_\mathrm{SL}} \right)^{5.256}
\label{eq:ISA:Ratios:Troposphere:Delta}
\end{equation}

\begin{equation}
\sigma (h) = \left( \frac{T(h)}{T_\mathrm{SL}} \right)^{\frac{g_0}{\lambda R} - 1}
  = \left( \frac{T(h)}{T_\mathrm{SL}} \right)^{4.256}
\label{eq:ISA:Ratios:Troposphere:Sigma}
\end{equation}
