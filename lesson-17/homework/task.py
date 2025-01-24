import numpy as np
import matplotlib.pyplot as plt

# Ensure you have Axes3D imported for 3D plotting
from mpl_toolkits.mplot3d import Axes3D  # Correct import for 3D plotting

# 1. Basic Plotting: Plot the function f(x) = x^2 - 4x + 4 for x between -10 and 10
x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4
plt.figure()
plt.plot(x, y, label=r'$f(x) = x^2 - 4x + 4$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = x^2 - 4x + 4')
plt.grid(True)
plt.legend()
plt.show()

# 2. Sine and Cosine Plot: Plot sin(x) and cos(x) for x from 0 to 2π
x = np.linspace(0, 2 * np.pi, 400)
sin_y = np.sin(x)
cos_y = np.cos(x)

plt.figure()
plt.plot(x, sin_y, label=r'$\sin(x)$', color='blue', linestyle='-', marker='o')
plt.plot(x, cos_y, label=r'$\cos(x)$', color='red', linestyle='--', marker='x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of sin(x) and cos(x)')
plt.legend()
plt.grid(True)
plt.show()

# 3. Subplots: Create a 2x2 grid of subplots with different functions
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Top-left: f(x) = x^3
x = np.linspace(-5, 5, 400)
y = x**3
axs[0, 0].plot(x, y, color='green')
axs[0, 0].set_title(r'$f(x) = x^3$')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')

# Top-right: f(x) = sin(x)
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x)
axs[0, 1].plot(x, y, color='orange')
axs[0, 1].set_title(r'$f(x) = \sin(x)$')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')

# Bottom-left: f(x) = e^x
x = np.linspace(0, 5, 400)
y = np.exp(x)
axs[1, 0].plot(x, y, color='purple')
axs[1, 0].set_title(r'$f(x) = e^x$')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')

# Bottom-right: f(x) = log(x + 1)
x = np.linspace(0, 5, 400)
y = np.log(x + 1)
axs[1, 1].plot(x, y, color='brown')
axs[1, 1].set_title(r'$f(x) = \log(x+1)$')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')

# Adjust layout and show plot
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Plot 100 random points
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.figure()
plt.scatter(x, y, color='magenta', marker='^')
plt.title('Random Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# 5. Histogram: Plot histogram of 1000 random values from a normal distribution
data = np.random.normal(0, 1, 1000)

plt.figure()
plt.hist(data, bins=30, color='cyan', alpha=0.7)
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 6. 3D Plotting: Plot f(x, y) = cos(x^2 + y^2) over x, y from -5 to 5
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)
z = np.cos(x**2 + y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, cmap='viridis')
fig.colorbar(surf)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.set_title('3D Surface Plot of f(x, y) = cos(x^2 + y^2)')
plt.show()

# 7. Bar Chart: Plot sales data for 5 products
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.figure()
plt.bar(products, sales, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.title('Sales Data for Products')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()

# 8. Stacked Bar Chart: Contribution of categories over time periods
categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
data = np.array([[5, 3, 2], [7, 4, 3], [6, 5, 4], [8, 3, 5]])

plt.figure()
plt.bar(time_periods, data[:, 0], label=categories[0], color='blue')
plt.bar(time_periods, data[:, 1], label=categories[1], color='green', bottom=data[:, 0])
plt.bar(time_periods, data[:, 2], label=categories[2], color='red', bottom=data[:, 0] + data[:, 1])
plt.title('Stacked Bar Chart of Categories Over Time Periods')
plt.xlabel('Time Periods')
plt.ylabel('Contribution')
plt.legend()
plt.show()
