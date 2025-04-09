import numpy as np
import sympy as sp


class Solver:
    def __init__(self, f, a, b, eps, max_iter, h):
        self.f_str = f
        self.f = sp.lambdify(sp.symbols('x'), f, "numpy")
        self.f_der = sp.lambdify(sp.symbols('x'), sp.diff(f, sp.symbols('x')), "numpy")
        self.a = a
        self.b = b
        self.eps = eps
        self.max_iter = max_iter
        self.h = h
        self.results = []

    def solve(self):
        x_values = np.arange(self.a, self.b, self.h)
        root_index = 0
        for i in range(len(x_values) - 1):
            x_0 = x_values[i]
            x_1 =  x_values[i + 1]
            if (self.f(x_0) == 0) or (self.f(x_1) == 0) or (self.f(x_0) * self.f(x_1) < 0):
                root_index += 1
                x0 = (x_0 + x_1) / 2.0
                if self.f_der(x0) == 0:
                    self.results.append((i, (x_0, x_1), None, None, 0, 1))
                    continue
                xn = x0
                iter_count = 0
                error_code = 0
                while iter_count < self.max_iter:
                    iter_count += 1
                    xn_1 = xn - self.f(xn) / self.f_der(x0)
                    if abs(xn_1 - xn) < self.eps:
                        xn = xn_1
                        break
                    xn = xn_1
                else:
                    error_code = 2
                self.results.append((root_index, (x_0, x_1), xn, self.f(xn), iter_count, error_code))
        return self.results

    def find_extrema(self):
        extrema = []
        x_values = np.linspace(self.a, self.b, 1000)
        y_der_values = self.f_der(x_values)
        for i in range(len(x_values) - 1):
            if y_der_values[i] == 0 or y_der_values[i] * y_der_values[i + 1] < 0:
                x0 = (x_values[i] + x_values[i + 1]) / 2.0
                extrema.append((x0, self.f(x0)))

        return extrema

    def find_inflections(self):
        inflections = []
        x_values = np.linspace(self.a, self.b, 1000)
        y_der2_values = sp.lambdify(sp.symbols('x'), sp.diff(self.f_str, sp.symbols('x'), 2), "numpy")(x_values)
        for i in range(len(x_values) - 1):
            if y_der2_values[i] == 0 or y_der2_values[i] * y_der2_values[i + 1] < 0:
                x0 = (x_values[i] + x_values[i + 1]) / 2.0
                inflections.append((x0, self.f(x0)))

        return inflections
