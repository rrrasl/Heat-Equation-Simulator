# Derivation of the Heat Equation and Finite Difference Scheme

## 1. Fourier's Law

Heat flows from regions of high temperature to regions of low temperature.

The heat flux is proportional to the temperature gradient:

q = -k dT/dx

where:

* q = heat flux
* k = thermal conductivity

The negative sign indicates that heat flows toward lower temperatures.

## 2. Energy Conservation

Consider a small rod element of length dx.

Heat enters from the left side and leaves from the right side.

The difference between incoming and outgoing heat causes the internal energy of the element to change.

Applying conservation of energy gives:

∂T/∂t = α ∂²T/∂x²

where α is the thermal diffusivity.

This equation is known as the one-dimensional heat equation.

## 3. Spatial Discretization

The rod is divided into equally spaced nodes.

The second spatial derivative is approximated using the central difference formula:

∂²T/∂x² ≈ (T[i+1] - 2T[i] + T[i-1]) / dx²

## 4. Time Discretization

The time derivative is approximated using a forward difference:

∂T/∂t ≈ (T_new[i] - T[i]) / dt

## 5. Explicit Finite Difference Scheme

Substituting both approximations into the heat equation gives:

T_new[i] = T[i] + r (T[i+1] - 2T[i] + T[i-1])

where:

r = α dt / dx²

This update equation is implemented in solver_1d.py.

## 6. Stability

The explicit finite difference method requires:

r <= 0.5

to ensure numerical stability.

Violating this condition causes oscillations and divergence of the solution.

