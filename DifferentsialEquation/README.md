# What is DifferentialEquation?
DifferenstialEquation is an equation that contains derivative of an unknown function is called a differential equation. 
The rate of a function at a poin is defined by the derivative of the function. A differential equation releases these derrivative 
with the other functions. Differential equations are mainly used in the fields of biology, physics, engineering, and many

## So what is the relationship between the differential and this project?
- Defining the differential Equation Function: In the code section `def pendulum(y, t, g, L)`, the function `pendulum` is defined
  to take the state vector `y` time `t` and parameters `g` and `L`. This function implements the differential equation of a simple
  pendulum , which is `-g/L * sin(theta)`, representing the angular accelartion of the pendulum as a function of time
- Solving the Differential Equation : In the code section `sol = odeint(pendulum, y0, t, args=(g, L)`, the differential equation of
  the simple pendulum is solved using the `odeint` function from the `scipy.integrate` module. This function takes the differential
  equation (`pendulum`), initial conditions (`y0`), time range(`t`), and additional arguments (`g` and `L`) to obtain the numerical solution
  of the differential equation
- Plotting Angle versus Time : Finally, in code section `plt.plot(t, sol[:,0])`, the numerical solution of the differential equation
  is used to plot the angle of the pendulum as a function of time, The plot demonstrates how the angle of the pendulum changes over time
