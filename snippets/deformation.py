import numpy as np
import matplotlib.pyplot as plt

def plot_deformed_grid(map_func, xlim=(-3, 3), ylim=(-3, 3), grid_size=20):
    """
    Plots a regular grid and its deformation by map_func.
    """
    # Create the original grid
    x = np.linspace(xlim[0], xlim[1], grid_size)
    y = np.linspace(ylim[0], ylim[1], grid_size)
    X, Y = np.meshgrid(x, y)

    # Apply the deformation function
    X_deformed, Y_deformed = map_func(X, Y)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 8))
    # Plot original grid in light grey
    for i in range(grid_size):
        ax.plot(X[i, :], Y[i, :], color='lightgrey', linewidth=1)
        ax.plot(X[:, i], Y[:, i], color='lightgrey', linewidth=1)
    # Plot deformed grid in blue
    for i in range(grid_size):
        ax.plot(X_deformed[i, :], Y_deformed[i, :], color='C0', linewidth=1)
        ax.plot(X_deformed[:, i], Y_deformed[:, i], color='C0', linewidth=1)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()

# Define a trigonometric deformation function
def wavy_deformation(x, y):
    return x + 0.5 * np.sin(2 * y), y + 0.5 * np.cos(2 * x)

# Generate the plot
# plot_deformed_grid(wavy_deformation)

## how to run
# start a python REPL in emacs (M-x run-python)
# from deformation_wavy import plot_deformed_grid, wavy_deformation
