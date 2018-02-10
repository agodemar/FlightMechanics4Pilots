---
layout: default
title: Types of Aircraft
categories: [menu, content, introduction]
permalink: /mypages/anatomy-conventional-aircraft/
---

# The Anatomy of Conventional Aircraft Configurations

This section introduces a set of definitions pertaining the architecture of conventional fixed-wing airplanes, which are useful in the discussion of aircraft performance characteristics as well as of aircraft stability and control. Since pilots already possess a knowledge of aircraft fundamentals by training, the various concepts are introduced here in view of an effective presentation of the flight theory as an engineering discipline. The knowledge of basic facts in aerodynamics is assumed.

## Aircraft Body Axes

The figure below represents an airplane with a conventional three-axis architecture aircraft. A reference frame $$\{ G, x, y, z \}$$ fixed with the vehicle is also shown.

{% include image.html
  url="/assets/img/ac_body_axes.png"
  width="80%"
  description="Aircraft body-fixed reference frame, with origin at CoG."
  %}

This cartesian reference is called *aircraft body-frame*. The origin $G$ coincides with the aircraft center of gravity (CoG) and the three axes are oriented as shown. For this reason the *body-axes* are also named $x_\mathrm{B}$, $y_\mathrm{B}$, and $z_\mathrm{B}$. The first axis $x_\mathrm{B}$ is directed along the fuselage longitudinal dimension and points forwards. The second body axis $y_\mathrm{B}$ is normal to the fuselage symmetry plane and is positively oriented towards the right wing tip. The third axis $z_\mathrm{B}$ completes the cartesian frame and points towards the fuselage belly.

## Planform definitions

The figure below shows a top view af an aircraft.

{% include image.html
  url="/assets/img/ac_topview.png"
  width="60%"
  description="Aircraft top view. Wing span $b=2s$."
  %}

Two of the quantities that characterize the wing planform are also shown:

- $b=2s$, the wing span;
- $\bar{c}$, the mean chord, taken over all the chords $c(y)$ at wing sections $y$ for $-\frac{b}{2} \le y \le +\frac{b}{2}$.

{% include image.html
  url="/assets/img/wing_basic.png"
  width="80%"
  description="A wing and its profiles (sections)."
  %}

The sections of a wing with planes parallel to the fuselage symmetry plane $x_\mathrm{B}z_\mathrm{B}$ have the shapes of airfoils. Wings owe to them its capacity to develop a lift force able to support the weight of the aircraft in flight, with a relatively small resistance.

## Wing-Fuselage definitions

A more detailed nomenclature is given by the next drawing, representing a top and a side view of a wing-fuselage combination.

{% include image.html
  url="/assets/img/ac_wing_fuselage_definitions_1.png"
  width="70%"
  description="Nomenclature of wing-fuselage combination (side view)."
  %}

The axes $x_\mathrm{C}$, $y_\mathrm{C}$, and $z_\mathrm{C}$ are what designers call *construction axes*. Like the body-axes, also the construction axes are fixed with the aircraft but are oriented differently. In the above illustration the various quantities are used to identify the position of the wing relative to the fuselage body. Typically, the body and construction axes $x_\mathrm{B}$ and $x_\mathrm{C}$ are parallel, but the latter is non-baricentric, originates at the fuselage nose and points backwards.

The quantities represented above have the following significance:

- $l_\mathrm{B}$, fuselage length;
- $b_\mathrm{B}$, $h_\mathrm{B}$, maximum fuselage width and fuselage height;
- $A$, wing apex point, i.e. leading edge of the wing root when wing leading edge line is ideally extended up to the symmetry plane;
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


## The Wing Zero-Lift Direction in Aircraft Configurations

An important angle, related to the lift capacity of the wing of a given aircraft, is that formed by the relative wind velocity vector $$\mathbf{V}_{\!\infty}$$ with the wing zero-lift direction. This direction is defined below.

### Wing Twist and Local Airfoil Zero-Lift Angles

The next figure shows a side view of a wing where the root and tip airfoils are emphasized.
All wing sections, at each possible spanwise station $-\frac{b}{2} \le y \le +\frac{b}{2}$, have a chord $c(y)$ which is geometrically twisted with respect to the root chord direction. The local geometric twist angle is called $\varepsilon_{\mathrm{g}}(y)$. The geometric twist is negative by definition if the local chord is pitched down with respect to the root chord --- this is called *wash out* angle by designers.

{% include image.html
  url="/assets/img/Wing_Twist.png"
  width="100%"
  description="Wing side view. Root and tip airfoils with local zero-lift lines."
  %}

The generic wing section at the station $y$ is an airfoil, i.e. an aerodynamic shape characterized by a local zero-lift direction inclined of an angle $\alpha_{0\ell}(y)$ with respect to the local chord --- a negative value for positively cambered profiles.
Therefore, the quantities represented above have the following significance:
- $\alpha_{0\ell,\mathrm{root}}$, zero-lift angle of the wing root airfoil;
- $\alpha_{0\ell,\mathrm{tip}}$, zero-lift angle of the wing tip airfoil;
- $\varepsilon_{\mathrm{g,tip}}$, geometric wing twist.

### Wing angle of attack

By definition, the angle of attack of a three-dimensional wing is the angle $\alpha_\mathrm{W}$ formed by the relative wind direction with the root chord line. A positive wing angle of attack is represented in the next figure.
It is important to recognize that the relative wind might invest the finite wing in such a way that the total lift $L$ developed by the surface is zero. The wing zero-lift direction is also represented below, forming an angle $\alpha_{0L,\mathrm{W}}$ with the root chord.

{% include image.html
  url="/assets/img/Alpha_Zero_Lift.png"
  width="100%"
  description="Wing side view. Wing zero-lift line."
  %}

The above picture shows a typical arrangement of wing airfoils, with the resulting wing zero-lift line pitched up with respect to the root chord. This corresponds to a negative wing angle of attack. Aerodynamicists elegantly explain that the lift of a wing is due to the *absolute angle of attack*

\begin{equation}
\alpha_{\mathrm{a,W}} = \alpha_{\mathrm{W}} - \alpha_{0L,\mathrm{W}}
\label{eq:Wing:Absolute:AoA}
\end{equation}

i.e. the angle between the relative wind and the zero-lift line. A zero absolute angle of attack means a zero wing lift; an $\alpha_{\mathrm{a,W}} < 0$ results in a downward oriented, hence negative, lift; a positive $\alpha_{\mathrm{a,W}}$ corresponds to a positive $L$.

### Aircraft angle of attack

From the above definitions, considering that a wing of a conventional aircraft is attached to the fuselage, from the perspective of flight an angle of attack *of the aircraft* is the angle $\alpha_\mathrm{B}$ formed by the relative wind with the reference axis $x_\mathrm{B}$ of the fuselage. This angle is also reported in the above figure.

### Wing Zero-Lift Line Representation in Aircraft Body-Axes

Consider a wings level flight, occurring along a horizontal trajectory of the CoG with no atmospheric wind. In this circumstance the vector $$\mathbf{V}_{\!\infty}$$ is horizontal and opposite to the flight velocity $\mathbf{V}$. A nonzero angle $\alpha_\mathrm{B}$ corresponds to a fuselage travelling with a pitched attitude with respect to the horizontal, as represented in the next figure. The effective angle formed by $$\mathbf{V}_{\!\infty}$$ and the wing zero-lift line is $\alpha_\mathrm{B} + i_\mathrm{w} - \alpha_{0L,\mathrm{W}}$, i.e. the *aircraft absolute angle of attack* $\alpha_\mathrm{a,B}$.


{% include image.html
  url="/assets/img/ac_longitudinal_symmetric_mux.png"
  width="80%"
  description="Wings level flight along a horizontal trajectory."
  %}

In the particular case of a flight with horizontal fuselage, i.e. $\alpha_\mathrm{B} = 0$, the aircraft absolute angle of attack becomes:

\begin{equation}
\mu_x = i_\mathrm{w} - \alpha_{0L,\mathrm{W}}
\label{eq:AC:mux}
\end{equation}

This angle is shown in the next figure.

{% include image.html
  url="/assets/img/ac_sideview_mu_x.png"
  width="90%"
  description="Aircraft side view and wing zero-lift line."
  %}

In a wings level flight, along a horizontal trajectory, with a zero pitching attitude of the fuselage, the angle $\mu_x$ is responsible for the lift supporting the aircraft (assuming, approximately, that the whole lift is given by the wing).

## Fuselage definitions

Some geometric parameters of a fuselage are represented in the next drawing.

{% include image.html
  url="/assets/img/fuselage_isoview_c172.png"
  width="100%"
  description="Nomenclature of the fuselage."
  %}

This figure shows the common definition of the two *aerodynamic angles* that define the orientation of the relative wind velocity vector with respect to the fuselage, and hence to the entire aircraft. These angles are $\alpha_\mathrm{B}$ --- already discussed above --- and the *sideslip* angle $\beta_\mathrm{B}$ (or simply $\beta$).

It might occur in flight that the relative wind is out of the aircraft symmetry plane. When the the pilot sees a current coming from the right it means that the aircraft is sideslipping with a positive angle $\beta$. This is the angle formed by the velocity vector $$\mathbf{V}_{\!\infty}$$ and the plane $x_\mathrm{C} z_\mathrm{C} = x_\mathrm{B} z_\mathrm{B}$. The projection of $$\mathbf{V}_{\!\infty}$$ into the plane is then used to measure the aircraft angle of attack $\alpha_\mathrm{B}$.


## The Horizontal Tailplane

The geometric parameters defining the position of the horizontal tailplane with respect to the fuselage are shown in the next two figures.

{% include image.html
  url="/assets/img/wing_fuselage_htail_definitions_1.png"
  width="100%"
  description="Nomenclature of the horizontal tailplane."
  %}

{% include image.html
  url="/assets/img/fuselage_isoview_c172_Htail.png"
  width="100%"
  description="Nomenclature of the horizontal tailplane."
  %}

The tailplane is anything other than a small wing placed in a rear position with respect to the main lifting surface. This is a traditional arrangement that ensures a longitudinal stability to the aerodynamic configuration.

{% include image.html
  url="/assets/img/htail_planform.png"
  width="70%"
  description="Horizontal tailplane planform."
  %}

{% include image.html
  url="/assets/img/horizontal_tail_profile.png"
  width="60%"
  description="Horizontal tailplane section."
  %}

{% include image.html
  url="/assets/img/horizontal_tail_profile_deltaE.png"
  width="60%"
  description="Elevator deflection."
  %}

{% include image.html
  url="/assets/img/horizontal_tail_profile_deltaE_deltaT.png"
  width="60%"
  description="Elevator and trim tab combined deflections."
  %}

## The Vertical Tailplane

{% include image.html
  url="/assets/img/fuselage_isoview_c172_Vtail.png"
  width="100%"
  description="Nomenclature of the vertical tailplane."
  %}

{% include image.html
  url="/assets/img/ac_rudder_control.png"
  width="100%"
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
