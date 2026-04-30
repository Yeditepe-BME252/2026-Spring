import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Create the original grid
x = np.linspace(-2, 2, 9)
y = np.linspace(-2, 2, 9)
X, Y = np.meshgrid(x, y)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.axis('off')
lines = []

# Create the initial grid lines
for i in range(len(x)):
    line, = ax.plot(X[i, :], Y[i, :], 'lightgrey', lw=1)
    lines.append(line)
    line, = ax.plot(X[:, i], Y[:, i], 'lightgrey', lw=1)
    lines.append(line)

# Add a small circle to visualize local deformation
circle = Circle((0, 0), 0.2, fill=False, color='red', lw=2)
ax.add_patch(circle)

# Update function for animation
def update(frame):
    t = frame / 10  # Time parameter from 0 to 1
    # Pure shear deformation: F = [[1, k(t)], [0, 1]]
    k = 2 * t  # Shear magnitude increases with time
    X_deformed = X + k * Y
    Y_deformed = Y
    
    # Update grid lines
    for i in range(len(x)):
        lines[i*2].set_data(X_deformed[i, :], Y_deformed[i, :])
        lines[i*2+1].set_data(X_deformed[:, i], Y_deformed[:, i])
    
    # Update the circle (approximated by a polygon)
    theta = np.linspace(0, 2*np.pi, 20)
    circle_x = 0.2 * np.cos(theta)
    circle_y = 0.2 * np.sin(theta)
    circle_x_deformed = circle_x + k * circle_y
    circle_y_deformed = circle_y
    circle.center = (0, 0)  # Update the center position
    #circle.set_xy(np.column_stack([circle_x_deformed, circle_y_deformed]))
    
    return lines + [circle]

# Create the animation
anim = FuncAnimation(fig, update, frames=21, interval=200, blit=True)

# Save as a GIF (requires imagemagick or pillow)
# anim.save('time_dependent_shear.gif', writer='pillow', fps=5)

plt.show()   
