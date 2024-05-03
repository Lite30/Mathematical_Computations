#Author : Liteboho Maseli 
#Date   : 03/05/2024
import matplotlib.pyplot as plt
import gradient as gd

# Plot the data points
plt.scatter(gd.data_df['x'], gd.data_df['y'], label='Data Points')

# Plot the straight line (model)
#x_line = gd.points.np.linspace(0, 10, 100)
y_line = gd.optimized_c + gd.optimized_m * gd.points.x_values
plt.plot(gd.points.x_values, y_line, color='red', label='Best-Fitting Line')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Graph with Best-Fitting Line')
plt.legend()
plt.grid(True)
plt.show()
