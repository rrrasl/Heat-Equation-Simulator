import numpy as np

class HeatSolver1D:
    def __init__(self, T, alpha, length, dt):
        self.alpha = alpha
        self.length = length
        self.dt = dt
        self.nx = len(T)
        self.dx = length / (self.nx - 1)
        self.T = T
        self.r = alpha * dt / self.dx**2
        self.curr_change = 100
        self.history = [self.T.copy()]

    def step(self):
        T_new = self.T.copy()

        for i in range(1, len(self.T) - 1):
            T_new[i] = (
                    self.T[i]
                    + self.r *
                    (
                            self.T[i + 1]
                            - 2 * self.T[i]
                            + self.T[i - 1]
                    )
            )
        T_temp = T_new - self.T
        self.curr_change = np.linalg.norm(T_temp)
        self.T = T_new
        self.history.append(T_new)
        print("T:\n" + str(T_new))
        print("Curr_change:\n" + str(self.curr_change)+"\n\n\n")

    def solve(self):
        while self.curr_change > self.alpha:
            self.step()
