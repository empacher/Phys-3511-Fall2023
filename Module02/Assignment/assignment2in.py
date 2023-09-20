#!/usr/bin/env python
# coding: utf-8

# # Assignment 2: Due Tuesday 9/19
# 
# ## 2D Projectile Motion with Quadratic Drag 
# 
# Quadratic drag term is given by $\vec{f}_{drag} = -cv\vec{v}$. This leads to equations of motion in the horizontal ($x$) and vertical ($y$) directions given by 
# 
# * $m v_{x}' = -\left(c\sqrt{v^2_x +v^2_y}\right)v_x$
# 
# * $m v_{y}' = - mg - \left(c\sqrt{v^2x + v^2_y}) \right)v_y$
# 
# * $x' = v_x$
# 
# * $y' = v_y$
# 
# ,where $'$ is a time derivative.
# 
# You can read more about drag forces here: https://openstax.org/books/university-physics-volume-1/pages/6-4-drag-force-and-terminal-speed

# ## Problem
# 
# To get an accurate trajectory for a projectile one must often take account of several complications. For example, if a projectile goes very high then we have to allow for the reduction in air resistance as atmospheric density decreases. To illustrate this, consider an iron cannonball (diameter, $D = 15\;cm$, density $\rho = 7.8\;g/cm^3$) that is fired with initial velocity $300 m/s$ at 50 degrees above the horizontal. The drag force is approximately quadratic, but since the drag is proportional to the atmospheric density and the density falls off exponentially with height, the drag force is $f = c(y) v^2$ where $c(y) = \gamma D^2 exp(-y/\lambda)$ with $\gamma$ given as $0.25\;N\cdot s^2/m^4$ and $\lambda = 10,000\;m$. 

# # Part a)
# 
# Ignoring air resistance completely, write down the equations of motion for the cannonball (use the markup feature in Jupyter notbook and latex (https://en.wikibooks.org/wiki/LaTeX/Mathematics)). Your answer should depend on only $v_x, v_y,$ and $g$ 

# Equations with no air resistance ($c = 0$):
# 
# * $v_x' = c$
# 
# * $x' =  v_x$
# 
# * $v_y' = -g$
# 
# * $y' = v_y$
#  

# Code the equations into a function 

# In[1]:


#define projectile motion function in vaccum
#def proj_vac

import math
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def proj_vac(t, y):
    g= 9.81
    c = 0
    
    x0 = y[2]
    y0 = y[3]
    vx0 = c
    vy0 = -g
    
    return [x0,y0,vx0,vy0]

y0 = [0,0,300*np.cos(np.pi /4), 300*np.sin(np.pi /4)]

time = (0, 50)  # 0to 50 s
t_eval = np.linspace(0, 50, 500)

solve = solve_ivp(proj_vac, time, y0, t_eval=t_eval, method = 'RK45')

x , y, vx, vy = solve.y

ground = solve.t[y <= 0][1]
range = x[y<= 0][-1]

#######################graph 

plt.plot(x,y)
plt.xlabel("horizontal")
plt.ylabel("vertical")
plt.show()


# Using Scipy (*RK4(5)* method) solve numerically $x(t)$ and $y(t)$ for $0 \le t \le 50\;s$

# In[ ]:


#code


# Plot the ball's trajectory (vertical vs. horizontal positions) and find it's horizontal range. At what time does the ball hit the ground?

# In[2]:


#codes


# # Part b)
# 
# Write your own Runge-Kutta order 4 function and use it to solve Part a) [Meaning do not use Scipy for this part].

# In[ ]:


#codes
import numpy as np
import matplotlib.pyplot as plt

#my own runge-kutta method

def runge(fun, y0, time, h):
    t0, tf = time
    n = int((tf - t0)/h)
    t = np.linspace(t0, tf, n)
    y = np.zeros((len(y0), n))
    y[:,0] = y0
    
    for i in range(1, n):
        a = h*np.array(fun(t[i-1], y[:, i-1]))
        b = h*np.array(fun(t[i-1]+ h/2, y[:, i-1] + a/2))
        c = h*np.array(fun(t[i-1]+ h/2, y[:, i-1] + b/2))
        d = h*np.array(fun(t[i-1]+ h, y[:, i-1] + c))
        
        y[:, i] = y[:, i-1] + (a + 2*b + 2*c + d) / 6
        
    return t, y

def proj_vac(t, y):
    g= 9.81
    return [y[2], y[3], 0, -g]

y0 = [0, 0, 300 *np.cos(np.pi/4), 300 * np.sin(np.pi /4)]

time = (0,50)
h = 0.1

t, y = runge(proj_vac, y0, time, h)

x, ym , vx, vy = y

ground = t[ym <= 0][0]
range = x[ym <= 0][0]

plt.plot(x,ym)
plt.xlabel("horizontal")
plt.ylabel("vertical")
plt.show()


# How does your Runge-Kutta 4th order evaluation compare to Scipy's *RK4(5)* method?

# # Part c)
# 
# Now include air resistance, but ignore the variation of atmospheric pressure [that is  treat $c(y)$ as a constant  that does not change with position, where $c = \gamma D^2$].
# 
# Write down the equations of motion (use the markup feature in Jupyter notbook and latex). Your answers should depend only on $c, m, v, v_x, v_y,$ and $g$.

# Equations with no air resistance ($c = const$):
# 
# * $v_x' = -\frac{c}{m}v_x\sqrt{v_x^2 + v_y^2}\$
# 
# * $x' = v_x$
# 
# * $v_y' = -g-\frac{c}{m}v_y\sqrt{v_x^2 + v_y^2}\$
# 
# * $y' =  v_y$

# Code the equations into a function

# In[3]:


#code


# Use Scipy (*RK4(5)* method) to solve numerically $x(t)$ and $y(t)$ for $0\le t \le 35\;s$

# In[4]:


#codes


# Plot the ball's trajecory and find it's horizontal range. At what time does the ball hit the ground?

# In[5]:


#codes


# # Part d)
# 
# Now include the drag term with the atmospheric variation included [meaning $c(y) = \gamma D^2exp(-y/\lambda)$]
# 
# Write down the equations of motion (use the markup feature in Jupyter notbook and latex). For this part write out explicitly what $c$ is in your equations, e.g. $a*c = a* \gamma D^2exp(-y/\lambda)$. Your equations should depend only on $\gamma, \lambda, y, D, v, v_x, v_y, m,$ and $g$.

# Equations with no air resistance ($c = \gamma D^2exp(-y/\lambda)$):
# 
# * $v_x' = $
# 
# * $x' = $
# 
# * $v_y' = $
# 
# * $y' = $

# Code the equations into a function

# In[ ]:


#code


# Use Scipy (*RK4(5)* method) to solve numerically $x(t)$ and $y(t)$ for $0\le t \le 35\;s$

# In[ ]:


#codes


# Plot the ball's trajectory and find it's horizontal range. At what time does it hit the ground?

# In[6]:


#codes


# # Part e)
# 
# Plot the trajectories from parts a), c), and d) on the same plot.

# In[7]:


#codes


# Your results should look like the plot below.
# 
# ![Final-Plots.png](attachment:Final-Plots.png)

# **What impacts the motion more: turning on air resistance (i.e with $c(0)$) or turning on the variation with atmosphere (i.e. $c(y)$) ?**

# In[ ]:




