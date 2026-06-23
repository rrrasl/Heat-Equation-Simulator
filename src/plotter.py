import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

def plot_snapshots(history, length):
    nx = len(history[0])
    x = np.linspace(0, length, nx)

    plt.figure()

    plt.plot(x, history[0], label="t = 0")
    plt.plot(x, history[len(history)//2], label="middle")
    plt.plot(x, history[-1], label="final")

    plt.xlabel("Position")
    plt.ylabel("Temperature")
    plt.title("Heat Diffusion Snapshots")
    plt.legend()
    plt.grid()

    plt.show()

def plot_multiple(history, length, n=5):
    nx = len(history[0])
    x = np.linspace(0, length, nx)

    step = max(1, len(history) // n)

    plt.figure()

    for i in range(0, len(history), step):
        plt.plot(x, history[i], label=f"t={i}")

    plt.xlabel("Position")
    plt.ylabel("Temperature")
    plt.title("Heat Diffusion Over Time")
    plt.legend()
    plt.grid()

    plt.show()


def animate(history, length):
    nx = len(history[0])
    x = np.linspace(0, length, nx)

    fig, ax = plt.subplots()
    line, = ax.plot(x, history[0])

    ax.set_ylim(min(map(min, history)), max(map(max, history)))
    ax.set_xlabel("Position")
    ax.set_ylabel("Temperature")

    def update(i):
        line.set_ydata(history[i])
        ax.set_title(f"Time step: {i}")
        return line,

    ani = FuncAnimation(fig, update, frames=len(history), interval=30)
    plt.show()


def interactive(history, length):
    nx = len(history[0])
    x = np.linspace(0, length, nx)

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    line, = ax.plot(x, history[0])
    ax.set_ylim(min(map(min, history)), max(map(max, history)))

    ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
    slider = Slider(ax_slider, 'Time', 0, len(history)-1, valinit=0, valstep=1)

    def update(val):
        i = int(slider.val)
        line.set_ydata(history[i])
        fig.canvas.draw_idle()

    slider.on_changed(update)

    plt.show()