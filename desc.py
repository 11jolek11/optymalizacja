from numpy import *
from numpy.linalg import norm

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.pyplot import *
from numpy import *


def f(x, y):
    pass

def dfdx(x, y):
    pass

def dfdy(x, y):
    pass

# $$$$$$$$$$$$$$$$$$
def f(x, y):
    return (x-1)*(y-1)*x*y + 0.5*((x-1)**2 + y**2 - 1)
    
def dfdx(x, y):
    return (2*x-1)*(y-1)*y
    
def dfdy(x, y):
    return (2*y-1)*(x-1)*x

# $$$$$$$$$$$$$$$$$$
def gradf(x, y):
    return array([dfdx(x, y), dfdy(x, y)])   

def grad_descent2(f, init_t, alpha):
    EPS = 1e-5
    prev_t = init_t-10*EPS
    t = init_t.copy()
    
    max_iter = 1000
    iter = 0
    while norm(t - prev_t) > EPS and iter < max_iter:
        print(iter)
        prev_t = t.copy()
        t -= alpha*gradf(t[0], t[1])
        # print(t, f(t[0], t[1]), gradf(t[0], t[1]))
        iter += 1
    return array(t)

if __name__ == "__main__":
    x = 0
    y = 5
    h = 0.001
    print(grad_descent2(f, array([1.0, 0.0]), 0.01))
