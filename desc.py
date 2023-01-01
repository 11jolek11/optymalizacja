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
    return x**2 + y**2
    
def dfdx(x, y):
    return 2*x
    
def dfdy(x, y):
    return 2*y

# $$$$$$$$$$$$$$$$$$
def gradf(x, y):
    return array([dfdx(x, y), dfdy(x, y)])   

def steepest_descent1(f, init_t, alpha):
    """
    Gradient descent - fixed step
    """
    # EPS = 1e-5
    EPS = 0.01
    prev_t = init_t-10*EPS
    # prev_t = init_t
    t = init_t.copy()
    
    max_iter = 1000
    iter = 0
    while norm(t - prev_t) > EPS and iter < max_iter:
        # print(iter)
        prev_t = t.copy()
        t -= alpha*gradf(t[0], t[1])
        # print(t, f(t[0], t[1]), gradf(t[0], t[1]))
        iter += 1
    print(f'After {iter} iterations.')
    return array(t)

if __name__ == "__main__":
    print(steepest_descent1(f, array([4.0, 4.0]), 0.3))