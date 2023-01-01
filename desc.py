from numpy import *
from numpy.linalg import norm
from matplotlib.pyplot import *
from numpy import *

def f(x, y):
    return x**2 + y**2
    
def dfdx(x, y):
    return 2*x
    
def dfdy(x, y):
    return 2*y

def gradf(x, y):
    return array([dfdx(x, y), dfdy(x, y)])   

def steepest_descent1(f, init_t, alpha, EPS=1e-5, history=False):
    """
    Steepest descent - fixed step
    """
    prev_t = init_t-10*EPS
    t = init_t.copy()
    history = {}
    max_iter = 1000
    iter = 0
    while norm(t - prev_t) > EPS and iter < max_iter:
        prev_t = t.copy()
        history.update({'iteration': iter, 'value': prev_t.copy()})
        t -= alpha*gradf(t[0], t[1])
        iter += 1
    print(f'After {iter} iterations.')
    if history:
        return array(t), history
    else:
        return array(t)

if __name__ == "__main__":
    print(steepest_descent1(f, array([4.0, 4.0]), 0.3, 0.01))
