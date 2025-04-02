import numpy as np
import sympy as sp


class Solver:
    def __init__(self, f, a, b, eps, max_iter, h):
        self.f_str = f
        self.f = sp.lambdify(sp.symbols('x'), f, "numpy")
        self.a = a
        self.b = b
        self.eps = eps
        self.max_iter = max_iter
        self.h = h
        self.results = []

    def solve(self):
        x_values = np.arange(self.a, self.b + self.h, self.h)
        for i in range(len(x_values) - 1):
            x_0 = x_values[i]
            x_1 =  x_values[i + 1]
            x0 = (x_0 + x_1) / 2.0
            if self.f(x0) == 0:
                self.results.append((i, (x_0, x_1), None, None, 0, 1))
                continue
            xn = x0
            iter_count = 0
            error_code = 0
            while iter_count < self.max_iter:
                iter_count += 1
                xn_1 = xn - self.f(xn) / self.f(x0)
                if abs(xn_1 - xn) < self.eps:
                    xn = xn_1
                    break
                xn = xn_1
            else:
                error_code = 2
            self.results.append((i + 1, (x_0, x_1), xn, self.f(xn), iter_count, error_code))
        return self.results

