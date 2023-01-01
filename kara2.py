from scipy.optimize import minimize, rosen
from math import sqrt
import numpy as np

def norm2(vector: list):
    vector_copy = vector.copy()
    for i in range(len(vector_copy)):
        vector_copy[i] = vector_copy[i]**2
    # print(vector_copy)
    return sqrt(sum(vector_copy))

# rz = lambda x: (1-x[0])**2 + 100*(x[1] - x[0]**2)**2
# h_1 = lambda x: (x[0] - 2 * x[1] + 2)
# h_2 = lambda x: (-x[0] - 2 * x[1] + 6)
# h_3 = lambda x: (-x[0] + 2 * x[1] + 2)

rz = lambda x: (x[0]+3)*(x[0]+1)*(x[0]-3)*(x[0]-1)*x[0]
h_1 = lambda x: (2*x[0]**3 - 4 * x[0] ** 2)
h_2 = lambda x: (-x[0]**3 - 2 * x[0]**2)


x0 = [2.3, 5]
cons = ({'type': 'ineq', 'fun': h_1},
       {'type': 'ineq', 'fun': h_2},) 
# print(minimize(rz, x0, constraints=cons).x)

# # TODO: correct
cache = []
EST = 0.01
# x_c = np.asarray([2.3, 3])
x_c = np.asarray([1])
i = 0
c = 0.5
while True:
    i += 1
    print(i)
    cache.append(x_c)
    curr_func = lambda x: rz(x) + c*(max(0, h_1(x))**2 + max(0, h_2(x))**2)
    # curr_func = lambda x: rz(x) + i*(max(0, h_1(x)) + max(0, h_2(x)) + max(0, h_3(x)))
    # curr_func = lambda x: rz(x) + i*(h_1(x)**2 + h_2(x)**2 + h_3(x)**2)
    x_c = minimize(curr_func, x_c, method="CG").x
    # print(cache)
    # TODO: add stop
    print(x_c)
    print(x_c - cache[-1])
    if norm2(x_c - cache[-1]) < EST:
        break
    c  *= 2
print('##########################333')
print(x_c)