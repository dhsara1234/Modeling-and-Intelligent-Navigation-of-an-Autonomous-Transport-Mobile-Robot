
import numpy as np
import matplotlib.pyplot as plt

# Define environment size
env_size = 20
start_position = (19, 19)  # Bottom-right corner
end_position = (0, 0)  # Top-left corner

# Initialize the environment grid
env = np.zeros((env_size, env_size))

# Function to add a single point obstacle
def add_point(x, y):
    if (x, y) != start_position and (x, y) != end_position:
        env[x, y] = 1

# Function to add a line obstacle
def add_line(x, y, direction, length):
    for i in range(length):
        if direction == 'horizontal' and x + i < env_size and (x + i, y) != start_position and (x + i, y) != end_position:
            env[x + i, y] = 1
        elif direction == 'vertical' and y + i < env_size and (x, y + i) != start_position and (x, y + i) != end_position:
            env[x, y + i] = 1

# Function to add a rectangle obstacle
def add_rectangle(x, y, width, height):
    for i in range(width):
        for j in range(height):
            if x + i < env_size and y + j < env_size and (x + i, y + j) != start_position and (x + i, y + j) != end_position:
                env[x + i, y + j] = 1

# Function to add an L-shaped obstacle
def add_l_shape(x, y, size):
    add_line(x, y, 'vertical', size)
    add_line(x, y, 'horizontal', size)

# Add varied obstacles spread across the map
# Top-left quadrant
add_point(2, 2)
add_line(1, 5, 'horizontal', 4)
add_rectangle(3, 1, 2, 3)
add_l_shape(7, 3, 2)

# Top-right quadrant
add_point(17, 3)
add_line(13, 1, 'vertical', 5)
add_rectangle(16, 6, 3, 2)
add_l_shape(11, 2, 3)

# Bottom-left quadrant
add_point(3, 16)
add_line(1, 13, 'horizontal', 6)
add_rectangle(6, 15, 2, 4)
add_l_shape(4, 11, 2)

# Bottom-right quadrant
add_point(16, 17)
add_line(18, 12, 'vertical', 6)
add_rectangle(13, 15, 3, 2)
add_l_shape(15, 11, 3)

# Center area
add_point(10, 10)
add_line(8, 9, 'horizontal', 4)
add_rectangle(11, 7, 2, 2)
add_l_shape(7, 11, 2)

# Plot the environment
plt.figure(figsize=(10, 10))
plt.imshow(env, cmap='Greys', origin='upper')

# Add start and end positions
plt.plot(start_position[1], start_position[0], 'go', markersize=12, label='Start')
plt.plot(end_position[1], end_position[0], 'ro', markersize=12, label='End')

# Add grid and labels
plt.grid(which='both')
plt.xticks(np.arange(0, env_size, 1))
plt.yticks(np.arange(0, env_size, 1))
plt.gca().set_xticks(np.arange(-.5, env_size, 1), minor=True)
plt.gca().set_yticks(np.arange(-.5, env_size, 1), minor=True)
plt.gca().grid(which='minor', color='w', linestyle='-', linewidth=2)

# Add legend
plt.legend(loc='upper right')

plt.title("20x20 Grid Environment with Evenly Spread Varied Obstacles")
plt.show()

# Save the environment to a file
np.save('grid_environment.npy', env)
print("Environment saved to grid_environment.npy")
