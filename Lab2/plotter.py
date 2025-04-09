import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, solver):
        self.solver = solver

    def plot(self):
        x_plot = np.linspace(self.solver.a, self.solver.b, 1000)
        y_plot = self.solver.f(x_plot)
        plt.plot(x_plot, y_plot, label='f(x)')

        # Корни функции
        x_roots = [s[2] for s in self.solver.results]
        y_roots = [s[3] for s in self.solver.results]
        plt.plot(x_roots, y_roots, 'ro', markersize=3, label='корни')

        # Экстремумы функции
        extrema = self.solver.find_extrema()
        x_extrema = [s[0] for s in extrema]
        y_extrema = [s[1] for s in extrema]
        plt.plot(x_extrema, y_extrema, 'go', markersize=3, label='экстремумы')

        # Точки перегиба функции
        inflection_points = self.solver.find_inflections()
        x_inflection = [s[0] for s in inflection_points]
        y_inflection = [s[1] for s in inflection_points]
        plt.plot(x_inflection, y_inflection, 'bo', markersize=3, label='точки перегиба')

        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'{self.solver.f_str}')
        plt.legend()
        plt.grid(True)
        plt.show()