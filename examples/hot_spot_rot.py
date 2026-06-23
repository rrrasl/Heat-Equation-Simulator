import numpy as np

def ex1():
    depth = 100
    rod = []
    T0 = 20
    for _ in range(depth):
        rod.append(T0)

    rod[depth//2] = 100

    return np.array(rod, dtype=np.float32)

