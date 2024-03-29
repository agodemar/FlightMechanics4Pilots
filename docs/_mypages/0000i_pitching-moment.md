---
layout: default
title: Pitching Moment
categories: [menu, content, intro, pitching-moment]
permalink: /mypages/pitching-moment/
---

# Aerodynamic Pitching Moment

## Center of Pressure (CP)

The aerodynamic interaction of a wing with an airflow determines a distribution of
varying local pressures and tangential stresses on the external surface. The surface exposed to the airflow
is also called the *wet surface* of the wing.
The same concept applies to all remaining parts of an aircraft, such as the external shape of the fuselage
as well as the wet surfaces of tailplanes.

The local pressures and tangential stresses, provided they are multiplied by the area $\mathrm{d}\mathcal{A}$
of the elemental wet surface, represent a *system of applied forces*. In general, these forces are non-coplanar
and non-parallel yet they can be resolved into an *equivalent single force* represented by the resultant,
applied along a well determined axis. The aerodynamic resultant $\boldsymbol{F}$ is a representative force which
has the same physical effect on a given body, in our case a wing or the entire aircraft, as the group of
forces it replaces.
In aerodynamics this conceptual process is known as *reduction* of the overall aerodynamic action of the
airflow on the airplane *to the resultant aerodynamic force*, applied to *center of pressure*.
Actually, the resultant can be applied to any given point of its line of action.

When airfoils are considered, the aerodynamic resultant is a force per unit span $\boldsymbol{f}$
applied on a point on the chord, i.e. the center of pressure of airfoils is located on the chord.
This is illustrated by the next figure. The vectors $\boldsymbol{n}$ are the local unit vectors normal to the
airfoil and pressure difference vectors $(p-p_\infty)\boldsymbol{n}$ represent the local normal strains exerted
on the airfoil external shape by the flow. These vectors, multiplied by the small areas
$\mathrm{d}\mathcal{A} = \mathrm{d}s\cdot 1\,\mathrm{m}$ (where $\mathrm{d}s$ is the element of curvilinear
abscissa running along the airfoil and $1\,\mathrm{m}$ is the unit spanwise length) are forces distributed on
the external surface of the airfoil. A symilar system of vector exists and is represented by the vectors
$\tau_\mathrm{w}\boldsymbol{t}$, where $\tau_\mathrm{w}$ are the local viscous tangential stresses and
$\boldsymbol{t}$ are the local unit vectors tangent to the airfoil. The ensemble of all these force vectors
applied on the airfoil contour give rise to the the resultant $\boldsymbol{f}$ shown below.

{% include image.html
  url="/assets/img/Airfoil_Pressures_Reduction.png"
  width="70%"
  description="Reduction of pressure distribution over the airfoil external surface to the aerodynamic resultant force $f$ applied to the center of pressure (CP)."
  %}

The system of all local external forces on the airfoil, due to the airflow of asymptotic speed $V_\infty$ at an angle
of attack $\alpha$, *is equivalent* to the resultant $\boldsymbol{f}$, which is *reduced* to the center of pressure
$\mathrm{CP}$. Therefore, to the point $\mathrm{CP}$ are applied both the lift per unit span $\ell$ and the drag per
unit span $d$.

The same is done for finite wings for which the center of pressure is taken on the root chord, i.e. the resultant
$\boldsymbol{F}_\mathrm{W}$ acts in the plane of symmetry.

{% include image.html
  url="/assets/img/Wing_Alpha_Pressure_Reduction.png"
  width="100%"
  description="External aerodynamic actions on a wing reduced to the aerodynamic resultant force $F_\mathrm{W}$ applied to the center of pressure (CP) on the root chord."
  %}

Due to the high values of aerodinamic efficiencies of airfoils and wings, often one can *neglect the drag component*
in the above constructions, i.e. $d\approx 0$ and $D_\mathrm{W}\approx 0$.

## Aerodynamic Center

The figure below represents an airfoil at a given angle of attack $\alpha$.
The pressure and tangential stress distributions on the airfoils are reduced, if one neglects the drag,
to the sole lift $\ell$ applied to the center of pressure.
It is known from aerodynamics that, for a fixed airspeed $V_\infty$, an *increasing angle of attack*
determines an increase of $\ell$ and a movement of the point $\mathrm{CP}$ along the chord
*towards the leading edge*. This forward shift takes place until $\alpha$ reaches the stall angle
of attack $\alpha_\mathrm{stall}$ of the airfoil then, for a further increase of $\alpha$, the center
of pressure starts moving backwards.

{% include image.html
  url="/assets/img/Airfoil_Pressures_Reduction_Simplified.png"
  width="70%"
  description="Approximated reduction of airfoil pressure distribution to the lift $\ell$ applied to the center of pressure (CP)."
  %}

On the other end, for decreasing $\alpha$'s the center of pressure shifts backwards while $\ell$
decreases. The point $\mathrm{CP}$ tends to move infinitely downstream as $\alpha$ approaches the
angle $\alpha_{0\ell}$ and $\ell$ tends to zero.

It should be noted that, being the system of external aerodynamic forces equivalent to the force
$\ell$ applied in $\mathrm{CP}$, the moment $m_P$ per unit span of aerodynamic forces with respect to
a given pole $P$ is equal to the moment of the reduced system with respect to $P$.
The figure below explains this concept.

{% include image.html
  url="/assets/img/Airfoil_Pressures_Moment_Simplified.png"
  width="70%"
  description="Airfoil pitching moment with respect to a pole $P$."
  %}

If $x$ is the arm of $\mathrm{CP}$ to $P$ the aerodynamic moment is

\begin{equation}
m_P = - \ell \, x
\label{eq:Airfoil:Moment:P}
\end{equation}

For $\ell$ and $x$ positive as shown, the resulting pitch-down couple is negative by definition.
If the angle of attack changes, both $\ell$ and $x$ will change and so will do $m_P$.

The variability of the aerodynamic reduction point $\mathrm{CP}$ is an unfavourable circumstance
when the aerodynamic behaviour of wings and tailplanes have to be evaluated to assess the pitching
equilibrium or pitching dynamics of a complete aircraft.
Fortunately, the experimental evidence confirms the existence of a particular *focal point* along the
chord of airfoils that exhibits a unique property: the pitching moment of the lift with respect to
this point is invariant with the angle of attack. This particular pole is called *aerodynamic center*
(ac) and for slender airfoils it is located approximately at a distance of $c/4$ from the leading edge.

A qualitative plot of the airfoil moment coefficient with respect to the quarter chord point
\begin{equation}
C_{m_{c/4}} = \frac{m_{c/4}}{\frac{1}{2}\rho V^2 c^2}
\label{eq:Airfoil:Moment:c4}
\end{equation}

is reported in the next figure.

{% include image.html
  url="/assets/img/Airfoil_Cmc4_Vs_alpha_curve.png"
  width="60%"
  description="Airfoil pitching moment coefficient with respect to a pole at the quarter-chord versus angle of attack."
  %}

The non-variability of $C_{m_{c/4}}$ of airfoils with the angle of attack is well explained by the following figure,
where four conditions of increasing $\alpha$ are considered.

- In the first condition, at an angle $\alpha = \alpha_{0\ell}$, the $\mathrm{CP}$ is located ideally at a distance
  $x\rightarrow\infty$   from the pole, yet the lift $\ell = 0$. The aerodinamic pressures and tangential stresses
  at the profile surface have a zero resultant but are not null, and their resultant pitching moment with respect
  to the pole is non-null either being equal to $C_{m_0}$. In such a case, when the resultant is zero, the
  aerodynamics of the airfoil is reduced to a sole *free couple*.
- In the subsequent conditions, from 3 to 4, the resultant $\ell$ is not null but the advancing $\mathrm{CP}$ and
  the increasing lift are such that the product $-\ell\,x$ remains equal to $C_{m_0}$.

{% include image.html
  url="/assets/img/Airfoil_Center_Pressure.png"
  width="90%"
  description="Airfoil center of pressure (CP) variation with angle of attack. System reduction to the aerodynamic center at $c/4$ (approximately)."
  %}

The four conditions considered in the previous figure are reported below on the curves of
$C_\ell$ and $C_{m_{c/4}}$ as functions of $\alpha$. It must be noted that the existence of a
focal point is justifiable strictly for those angles of attack within the $C_\ell$ linearity range.

{% include image.html
  url="/assets/img/Airfoil_CL_Cmc4_Vs_alpha_curve.png"
  width="90%"
  description="The four conditions considered in the previous figure. As the $\alpha$ changes in the $C_\ell$ linearity range the airfoil $C_{m_{c/4}}$ remains invariant."
  %}

Finite wings are three-dimensional lifting surfaces that have the same characterisics of airfoils.
Therefore, an aerodynamic center also exists for wings. As shown in the next top view of a wing,
in the three-dimensional case the focal point 'ac' is in the symmetry plane, somewhere on the
root chord or, according to the situation, on the projection of the mean aerodynamic chord.

{% include image.html
  url="/assets/img/Wing_Topview_Aerodynamic_Center.png"
  width="80%"
  description="Wing top view showing the mean aerodynamic chord $\bar{c}$ and the wing aerodynamic center."
  %}

For wings one can speak of *focal axis*, i.e. a pitch axis passing through the aerodynamic center
and such that the pitching coefficient

$$
C_{\mathcal{M}_\mathrm{ac}} = \frac{\mathcal{M}_\mathrm{ac}}{\frac{1}{2}\rho V_\infty^2 S \, \bar{c}} = \mathrm{const}
\label{eq:Wing:Moment:ac}
$$

This is confirmed by the next plot for all angles of attack
$\alpha_{0L,\mathrm{W}} \le \alpha_\mathrm{W} \le \alpha_\mathrm{W}^\star$.

{% include image.html
  url="/assets/img/Wing_Cmac_Vs_alpha_curve.png"
  width="60%"
  description="Wing pitching moment coefficient with respect to aerodynamic center versus angle of attack."
  %}

The existence of the aerodynamic center of wings, i.e. a pitch focal axis, is such a favourable circumstance:
as the angle of attack changes, the aerodynamic effect of the airflow over the lifting surface can be
reduced to the lift $L_\mathrm{W}$ applied to the fixed point 'ac' *and* to a constant moment
$\mathcal{M}_\mathrm{ac}$ about the same pole.

A very important practical outcome of this circumstance is illustrated by the next figure.
When one needs to evaluate the aircraft baricentric pitching moment due to the aerodynamics
of the wing, it can be simply calculated by multiplying $L_\mathrm{W}$ times the arm $a$ and then adding the couple
$\mathcal{M}_\mathrm{ac,W}$.

{% include image.html
  url="/assets/img/ac_sideview_wing_mac_simplified.png"
  width="100%"
  description="Reduction of wing aerodynamics. Lift $L_\mathrm{W}$ applied to the wing aerodynamic center and pitching moment $\mathcal{M}_\mathrm{ac,W}$."
  %}

Therefore, the pitching moment
$$\mathcal{M}_{G,\mathrm{W}}$$
of the wing about the aircraft center of gravity $G$ is:

$$
\mathcal{M}_{G,\mathrm{W}} = \mathcal{M}_\mathrm{ac,W} + L_\mathrm{W} \, a
\label{eq:Wing:Moment:G}
$$

The corresponding pitching moment coefficient

$$
C_{\mathcal{M}_G,\mathrm{W}} = \frac{\mathcal{M}_{G,\mathrm{W}}}{\frac{1}{2}\rho V_\infty^2 S \, \bar{c}}
\label{eq:Wing:CM:G:A}
$$

can be calculated considering that

$$
L_\mathrm{W} = \frac{1}{2}\rho V_\infty^2 S \, C_{L_{\alpha}\mathrm{,W}} \big(\alpha_\mathrm{B} + i_\mathrm{W} - \alpha_{0L\mathrm{,W}}\big)
$$

and substituting into the expression (\ref{eq:Wing:Moment:G}), to obtain the equation:

$$
C_{\mathcal{M}_G,\mathrm{W}} =  C_{\mathcal{M}_\mathrm{ac},\mathrm{W}} + C_{L_{\alpha}\mathrm{,W}} \big(\alpha_\mathrm{B} + i_\mathrm{W} - \alpha_{0L\mathrm{,W}}\big) \frac{a}{\bar{c}}
\label{eq:Wing:CM:G:B}
$$

The above expression can be rearranged as the following linear formula in $\alpha_\mathrm{B}$:

$$
C_{\mathcal{M}_G,\mathrm{W}} =  {\color{green}{ C_{\mathcal{M}_0,\mathrm{W}} }} + {\color{green}{ C_{\mathcal{M}_{\alpha}\mathrm{,W}} }}\; {\color{blue}{ \alpha_\mathrm{B} }}
\label{eq:Wing:CM:G:C}
$$

where the two constants are defined as:

$$
{\color{green}{ C_{\mathcal{M}_0,\mathrm{W}} }} = C_{\mathcal{M}_\mathrm{ac},\mathrm{W}} + C_{L_{\alpha}\mathrm{,W}} \big( i_\mathrm{W} - \alpha_{0L\mathrm{,W}} \big) \frac{a}{\bar{c}}
\label{eq:Wing:CM:G:D}
$$

$$
{\color{green}{ C_{\mathcal{M}_{\alpha}\mathrm{,W}} }}= C_{L_{\alpha}\mathrm{,W}} \; \frac{a}{\bar{c}}
\label{eq:Wing:CM:G:E}
$$

The above two constants are known by the designers, for a given flight condition, once the geometry of the wing
and the center of gravity position are known.

## Effect of the fuselage

When a wing-fuselage configuration is considered, also called *wing-body* by engineers, the concept of
aerodynamic center (or focal pitch axis) remains.
Fuselages of conventional airplanes develop almost no lift but are subject to a pitching moment due to
airflow. By adding the fuselage to the wing it can be shown that their combination still exhibits an aerodynamic
center.

The figure below shows a side view of an airliner.

{% include image.html
  url="/assets/img/B747_fuselage_sideview_1.png"
  width="100%"
  description="Boeing 747 fuselage side view."
  %}

This particular shape, when immersed in an air stream at an angle of attack $\alpha_\mathrm{B}$, generates
a pitching moment $\mathcal{M}_{\mathrm{B}}$.
A typical behaviour of this kind of stretched, cylinder-like shapes is shown in the next plot
representing the pitching moment coefficient of the fuselage

$$
C_{\mathcal{M},\mathrm{B}} = \frac{\mathcal{M}_{\mathrm{B}}}{\frac{1}{2}\rho V_\infty^2 S \, \bar{c}}
\label{eq:Body:CM}
$$

as a function of the angle of attack.

{% include image.html
  url="/assets/img/B747_fuselage_Cm_vs_alpha.png"
  width="70%"
  description="Boeing 747 fuselage pitching moment. The effect of the wing presence is included."
  %}

The positive slope of the above linear dependency from $\alpha_\mathrm{B}$
is un unfavourable circumstance for the longitudinal stability of airplanes.
<p>
The aircraft longitudinal stability is discussed in more detail
{% include search_page_put.html
  page_category='longitudinal-stability'
  put_text='in the section on pitch stability and control' %}.
</p>

The important practical outcome of the above discussion is illustrated by the next figure.
When one considers the wing-fuselage (WB) combination, typically *the aerodynamic center shifts forwards*
with respect to the original position determined for the isolated wing (W). Therefore, in the top view
reported below the wing-body aerodynamic center is located at the distance
$x_{\mathrm{ac,WB}}$ from the leading edge of the wing aerodynamic chord $\bar{c}$, which is
less than the distance $x_{\mathrm{ac,W}}$ of the focal axis of the isolated wing.

{% include image.html
  url="/assets/img/B747_fuselage_topview_2_en.png"
  width="100%"
  description="Boeing 747 wing-fuselage configuration. Aerodynamic center of the isolated wing and of the wing-body ombination."
  %}

In other terms, *the presence of the fuselage does not add a significant lifting capacity to the wing
but moves the aerodynamic center towards the nose*.
