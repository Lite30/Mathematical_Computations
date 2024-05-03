#Author : Liteboho Maseli 
#Date   : 03/05/2024

import numpy as np
import pandas as pd

# Set the number of data points (N)
N = 50
m = 3  # Slope
c = 2  # Y-intercept

def generate_data(N, c, m, noise_level=0.1):
    x = np.random.rand(N)
    noise = noise_level * np.random.randn(N)
    y = c + m * x + noise
    return x, y

# Generate random x-values within a specified range (e.g., 0 to 10)
x_values, y_values = generate_data(N,c,m)


# Create a DataFrame to store the data
df = pd.DataFrame({'x': x_values, 
                        'y': y_values})

# Save the data to a CSV file
df.to_csv('lite_data.csv', index=False)


