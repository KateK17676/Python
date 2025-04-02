import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, solver):
        self.solver = solver

    def plot(self):
        x_plot = np.linspace(self.solver.a, self.solver.b, 1000)
        y_plot = self.solver.f(x_plot)
        plt.plot(x_plot, y_plot, label='f(x)')

        x_roots = [s[2] for s in self.solver.results]
        y_roots = [s[3] for s in self.solver.results]
        plt.plot(x_roots, y_roots, 'ro', label='корни')

        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'{self.solver.f_str}')
        plt.legend()
        plt.grid(True)
        plt.show()