from scipy.optimize import minimize, rosen
rz = lambda x: (1-x[0])**2 + 100*(x[1] - x[0]**2)**2;
h_1 = lambda x: (x[0] - 2 * x[1] + 2);
h_2 = lambda x: (-x[0] - 2 * x[1] + 6);
h_3 = lambda x: (-x[0] + 2 * x[1] + 2);

x0 = [2.3, 5];
cons = ({'type': 'ineq', 'fun': h_1},
       {'type': 'ineq', 'fun': h_2},
       {'type': 'ineq', 'fun': h_3}) 
minimize(rz, x0, constraints=cons)

# TODO: correct
x_c = [2.3, 3]
i = 1
while i < 1000:
    curr_func = lambda x: rz(x) + i*(h_1(x)**2 + h_2(x)**2 + h_3(x)**2)
    x_c = minimize(curr_func, x_c).x
    i  *= 1.2
print(answer.x)