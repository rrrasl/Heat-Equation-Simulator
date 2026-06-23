from src.solver_1d import HeatSolver1D
import src.plotter as plt
import examples.hot_spot_rot as ex
from src.materials import MATERIALS


solver1 = HeatSolver1D(
    T=ex.ex1(),
    alpha=MATERIALS["copper"],
    length=1.0,
    dt=0.01
)

solver1.solve()
history = solver1.history

plt.interactive(history, solver1.length)