---
title: Chapter 4. Nesterov Acceleration
published: true
layout: page
sidebar: mydoc_sidebar
permalink: NesterovAcceleration.html
folder: monograph
---


# Erratum in Chapter 4. Nesterov Acceleration

## Section 4.2 -- Gradient Method and Potential Functions
### Section 4.2.3 --- How Conservative is this Worst-case Guarantee?

The definition of $f(x)$ should contains $+ b_\tau$, not $-b_\tau$:
\[
f(x)
\begin{cases}
  a_\tau |x| \textcolor{red}{+} b_\tau & \text{if } |x| \geq \tau, \\ 
  \tfrac{L}{2} x^2 & \text{otherwise}, 
  \end{cases}
\]
