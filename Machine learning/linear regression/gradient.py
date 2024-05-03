#Author : Liteboho Maseli 
#Date   : 03/05/2024
import points
# Load the data from the CSV file
data_df = points.pd.read_csv('random_data.csv')

def gradient_descent(x, y, learning_rate, iterations):
    c = 0
    m = 0
    n = len(x)
    for _ in range(iterations):
        y_pred = c + m * x
        error = y_pred - y
        c -= learning_rate * (1/n) * points.np.sum(error)
        m -= learning_rate * (1/n) * points.np.sum(error * x)
    return c, m

# Set the learning rate
learning_rate = 0.01
# Define the number of iterations
iterations = 1000

optimized_c, optimized_m = gradient_descent(points.x_values, 
                                            points.y_values, 
                                            learning_rate, 
                                            iterations)

# Final values of c and m
print(f"Optimal c: {optimized_c:.4f}")
print(f"Optimal m: {optimized_m:.4f}")
