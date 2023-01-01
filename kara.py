import sympy
import scipy
import math
import numpy as np


class Solver:
    def __init__(self, func: str, x: list) -> None:
        print('starting')
        self.funct = func
        self.start = x
        # self.run()

    @staticmethod
    def gen_cost_fun(point: np.array,h: list=[], g: list=[]):
        x, y = point[0], point[1]
        part_g = []
        part_h = []
        if g:
            for boundary in g:
                if eval("lambda x, y:" + boundary, math.__dict__)(x, y) > 0:
                    part_g.append(f'({boundary})**2')
        
        if h:
            for boundary in h:
                part_h.append(f'{boundary}**2')

        part_g = ' + '.join(part_g)
        part_h = ' + '.join(part_h)
        return part_h + ' + ' + part_g

    @staticmethod
    def func_wrapper(cls,x: list, temp_func: str):
        func = eval("lambda x, y:" + temp_func, math.__dict__)(x[0], x[1])
        return func

    @staticmethod
    def minimize(self, start_point: list):
        print(self.func_wrapper(start_point, self.funct))

    def run(self):
        print('running')
        calc = scipy.optimize.minimize(self.minimize, self.x)
        print(calc)

if __name__ == "___main__":
    p = Solver("x**2+y**2", [4, 4])
    p.run()
