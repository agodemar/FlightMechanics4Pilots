---
layout: post
title: Embedding into linear algebra
category: extra
---

Linear algebra is a powerful language that can embed other more interesting languages/systems/grammars/...? For example, computation, dual numbers, holographic representations, ???
Others? What about graphics, or ??, or


# Linear operators that can be embedding in LinAlg

Why is this cool? It is a general way to represent things. The power comes from it ability to make different operators by simply changing structure?

But are these more that just nice mathematical curiosities? Why is this useful or important?

##### Dual numbers

> the dual numbers extend the real numbers by adjoining one new element $\epsilon$ with the property $\epsilon^2 = 0$.

<side>Is this a functor? A transformation that preserves the structure?</side>

$$
a + b\epsilon \rightarrow
\begin{bmatrix}
a & b \\
0 & a \\
\end{bmatrix} \\
$$


$$
\begin{align*}
 (a + b\epsilon)(c + d\epsilon) &= ac + ad\epsilon + bc\epsilon + bd\epsilon^2\\
 &= ac + (ad + bc)\epsilon \\
\begin{bmatrix}
a & b \\
0 & a \\
\end{bmatrix}
\begin{bmatrix}
c & d \\
0 & c \\
\end{bmatrix}
&=
\begin{bmatrix}
ac & ad + bc \\
0 & ac \\
\end{bmatrix}
\end{align*} \\
$$


##### Complex numbers

$$
\begin{align}
a + b i \equiv
\begin{bmatrix}
a & b \\
-b & a \\
\end{bmatrix}
\end{align}
$$

##### Logic and (quantum) computation


$$
\begin{align}
CNOT \equiv
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 \\
\end{bmatrix}
\end{align}
$$

##### Differentiation

In the space of polynomials.

\begin{align*}
\frac{d}{dx} &= \begin{bmatrix}
0 & 1 & 0 & 0 & \dots \\
0 & 0 & 2 & 0 &  \dots \\
0 &0 & 0 & 3 & \dots \\
\vdots & \vdots & \vdots & \vdots & \ddots \\
\end{bmatrix}
\end{align*}

each column is the derivative of a 'basis' function, which in this case is each $x^n$.




### Memory

[Holographic reduced representations](http://www2.fiit.stuba.sk/~kvasnicka/CognitiveScience/6.prednaska/plate.ieee95.pdf)



### Type-systems

Strongly typed …


### Functions?




# Other ?

### What would we want them to do?

What would a non-linear and differentiable language for structure look like? What language would allow me to differentiably learn, say, a convolution?


### data structures!!

What alternatives are there to representing information that rival linear algebra?
* Trees and recursion (which actually ties into linalg - H-Tucker decomposition -- see other post on SVD).
* Graphs as adjacency matricies.
* ???
* Fields
*


# Thoughts

Why is linear algebra such an effective language for thinking about and expressing structure in systems?
What makes it so good? Is it really that great?
