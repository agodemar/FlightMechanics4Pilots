---
layout: post
title: Recursive optimisation
---


Imagine you have a parameterised optimisation function (e.g. SGD) which you use to find good minima of other parameterised functions, e.g. neural networks.

I want to know the best way to optimise a given (type of) function, e.g. CNNs. How can I do this? Optimise the optimiser?

So this is also know as hyperparameter optimisation or meta-learning. The techniques used are ... grid/random searches ...???

Instead, could we use the optimiser we already have? Afterall, optimisation is just a function. We have a loss function, the number of steps required to get to a minima, or the ...



### Verson 0.1

For simplicity we consider SGD as a parameterised function (parameterised by the learning rate).

```python
#A simple function to be optimised
def f(x):
    return x*2

#A simple convex optimiser with a single parameter
def optimise(func,params):
    while x[steps+1]-x[steps] > tolerance:
        x[steps+1] = x[steps] - params * grad(func,x[steps])
        steps +=1
    return x,steps

#Recursively call the optimiser on itself
def recusrive_optimiser(func,params,depth):
    if depth == 1:
        return optimise(f,params)
    else:
        return optimise(recursive_optimiser,params,depth-1)


def g(x):
    return x*4

min_f,params = recursive_optimiser(f,init,3)
min_g,params = recursive_optimiser(g,params,3)
```

* Wont this result in all optimisers (with a call) having the same parameters?
* So weight tying across optimisers, how does this make sense?
* What should I be doing with the outputs of the optimisers, while deep in the recursion?
* How is this related to data points and gradients evaluated at a point?
* The point is that it optimises a function as well as itself (to optimise the function faster).
* What does depth mean here? I get what depth two means, optimise the optimiser. But what does more depth do?
* What relation is there to higher order moments or second order methods?

### Verson 0.2

Just taking one step in the right direction from data. So the optimier should look at how much the step taken reduced the loss function and seek to maximise the reduction? Could this lead to poor places?

```python
#A simple function to be optimised
def f(x):
    return x*2

#Recursively call the optimiser on itself
def recusrive_optimiser(func,params,depth):
    if depth == 1:
        return x - params * grad(func,x[steps])
    else:
        return

```



> <i>I see 3 potential challenges with the recurrent setup, but i guess they all can be solved somehow:
1. Gradient for the task at hand and the optimizer have different distributions. This may be a problem, especially if the gradfients in one of the problems are much bigger (the optimizer would then just disregard the other task almost completly).
2. Different coordinates of lstm optimizers also have different distributions of gradient (bias vs connections, different lstm layers). This was a problem we encountered on cifar and we had to use 2 separator optimizers to mitigate it.
3. I guess that the optimizer could easily diverge because of the recurrent relationship if you don't entourage stability somehow (L2 penalty?).</i>


Some sort of batch normalisation of gradients seems like it could help with 1.? Nope. Where are the batches...?
