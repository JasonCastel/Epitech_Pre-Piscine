import numpy as np
import matplotlib.pyplot as plt
import math

def plot_fct(func, x_min, x_max, num_points=1000, subplot=None):
    # Vectorize the function to accept arrays as input
    func_vec = np.vectorize(func)
    
    # Generate x values
    x = np.linspace(x_min, x_max, num_points)
    
    # Evaluate the function for each x value
    y = func_vec(x)
    
    # If subplot is provided, plot on the specified subplot
    if subplot:
        plt.subplot(subplot)
    
    # Create the plot
    plt.plot(x, y, label=str(func.__name__))
    
    # Customize the plot
    plt.title("Function Plot")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()

# Create a single figure with multiple subplots
plt.figure(figsize=(12, 10))

# Plotting math.sin function
plot_fct(math.sin, 0, 50, subplot=221)  # Subplot 1

# Defining a custom function f(x)
def f(x):
    return x**2 + x*3 + 2

# Plotting custom function f(x)
plot_fct(f, -100, 200, subplot=222)  # Subplot 2

# Plotting a lambda function x^2
plot_fct(lambda x: x**2, -10, 10, subplot=223)  # Subplot 3

# Plotting a lambda function 1/x
plot_fct(lambda x: 1/x, -100, 100, subplot=224)  # Subplot 4

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
