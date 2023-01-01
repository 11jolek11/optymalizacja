from sympy import *



x, y, l = symbols('x y l')


print(solve([
    Eq(3*x**2-2*x*l, 0),
    Eq(3*y**2-2*y*l, 0),
    Eq(x**2+(y**2)-1, 0),
],
[x, y, l],
))

# from sympy import *

# s, t, l = symbols('s t l')

# print(solve([Eq((21/4)*((t**(1/4))/s**(1/4)) - 25*l, 0),
#    Eq((7/4)*(s**(3/4)/t**(3/4)) - 250*l, 0),
#    Eq(25*s+250*t - 2500, 0)], [s,t,l], simplify=False))

