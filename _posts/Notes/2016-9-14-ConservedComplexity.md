---
layout: post
title: Is complexity conserved?
---

Could the complexity of a problem/algorithm be a conserved quantity? (This is vaguely inspired by Scott Aaronson's [quip](http://www.scottaaronson.com/blog/?p=2212) about the latest claim that $P=NP$)

> All proposals along these lines simply _“smuggle the exponentiality”_ somewhere that isn’t being explicitly considered

I am imagining that each problem has some fixed amount of complexity, a set structure if you like. And our attempts to find efficient solutions cost us elsewhere. Like the conservation laws of energy, we can push around the complexity of our algorithm, we can squeeze it, or deform it, but the energy of the system remains the same. What we gain in mass we lose in momentum (energy-mass equivalence). What we gain in kinetic energy is lost in potential energy (falling down a hill). Or what we gain in time complexity we lose in sample complexity.

Increases in efficiency (that we see so regularly) may actually be _smuggling_ the complexity somewhere else. For example;

* increases in 'efficiency' of matmuls are actually costing us elsewhere. Maybe we are having to do more irreversible computations (which we probably wouldn't notice atm (?)).
* or what if there is too much data to store in a central location (bounded communication),
* or in a domain where we cannot assume IID
* or

$$
\begin{align*}
\mathcal{C}_{error} + \mathcal{C}_{robustness} = \mathcal{C}_{energy} + \mathcal{C}_{time} + \mathcal{C}_{memory} + \mathcal{C}_{parallel} + \mathcal{C}_{data} + \mathcal C_{privacy} = const.\\
\end{align*}
$$

This is about trade-offs.



### Thoughts

* What does this conservation of complexity imply about underlying structure and symmetries of problems and their algorithms?
<!-- * What about the domain that an algorithm works over. What sort of complexity measure do we have there? Should there be one?-->
<!--* How sure are we that each of these measures of complexity is the right metric?-->
* How can we represent problems/algorithms as structures?
    * What symmetries do these structures have?
    * Do all NP-complete problems share the same symmetries?
(I am struggling with the line between problem and solution, goal and algorithm)
