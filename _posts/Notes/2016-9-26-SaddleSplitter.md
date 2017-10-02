---
layout: post
title: A splitting architecture to break saddles?
---

How can we learn complicated, non-convex loss functions? The general idea behind [curriculum learning]() is to gradually learn more complex loss functions, while each intermetiate loss function is somehow related to your true goal. I like to think about this as a type of [transfer learning]() between the simpler learner (/loss function) to the more complex.

In the image below, we want to learn the deep network, the one on the right labelled $L4$. But the loss function (shown underneath in magenta) is just too complex, so how can we do it? How about transfering some knowledge of the task from simpler learners? (ignore the horizonal lines for now)

![pic]({{site.baseurl}}\images/Curriculum.png)

In general, there are a few different methods that can be used to transfer knowledge from simple learners to more complex;

* [Mollifying networks](https://arxiv.org/abs/1608.04980) transfer knowledge continuiously (?) from linear to (more) non-linear networks using ??!
* Reverse [Distillation](https://arxiv.org/abs/1503.02531) by training a deep network to mimic a more complex one, similar to feature matching
* In essence [Network morphism](https://arxiv.org/abs/1603.01670) solves a matrix decomposition of a layer (which can get complicated for non-linear layers)
* For those of you who have seen it before, the above picture may remind you of the [Fractal net](https://arxiv.org/abs/1605.07648) architecture. Interestingly, the fractal network uses a stoachastic path picking algorithm which allows the simpler networks to transfer their knowledge. (paths are randomly picked through each of the four learners by using the horizonal connections)


### Splitter

Inspired by the [Upstart](http://www.mitpressjournals.org/doi/abs/10.1162/neco.1990.2.2.198?journalCode=neco#.V-9IzZN96zY) algorithm, how can we use the above ideals and techniques to learn a more complex net from simpler ones?


```python
while Net.accuracy() < tol:
    Net.train_step()
    for layer in Net.Layers:
        if layer.learning_rate == slow:
            Net.layer.split()        #using network morphism
```

This algorithm is nice because we are increasing complexity only as necessary to accurately learn our target function. In an ideal world the algorithm would learn the shallowest network capable of accurately approximating our target function.


### Saddle breaking

The main question (for me) that comes of out this idea is whether reparameterising a weight matrix can free us from an obstacle in the loss surface. For example, if we have a simple linear autoencoder

$$\mathcal L = \parallel x - ABx\parallel_2^2$$

and we split $B$ into $CD$ such that $B = CD$ then does it help us learn faster? Intuitively, this feels somewhat like the kernel trick, where we can use the extra dimensionality of the reparameterised $CD$ to make our way around saddles or other obstacles in the loss surface.

[Deep learning without poor local minima](https://arxiv.org/abs/1605.07110) has an interesting note at the end of the appendices about how … ???


### HT decomposition

Start with a big wide network. Split the wide net into two matrices. ... This is doing a HT decomposition!! (??)
