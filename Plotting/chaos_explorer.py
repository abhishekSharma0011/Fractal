import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

def logistic_map(r=3.7, x0 = 0.5, iterations=100):
    x = x0
    xs = []
    for _ in range(iterations):
        x = r * x * (1 - x)
        xs.append(x)

    plt.figure(figsize=(10,5))
    plt.plot(xs,marker='o')
    plt.title(f'Logistic map for (r={r}) and (x={x})')
    plt.xlabel("Iterations")
    plt.ylabel("x")
    plt.show()

interact(logistic_map, r=(0,4,0.01), x0=(0,1,0.01), iterations=(10,500,10))