#author: Liteboho Maseli
#Date  : 03/05/2024
import math

def normal_pdf(x, mean, std_dev):
    """
    Calculate the probability density function of a normal distribution.
    
    Parameters:
        x (float): The value at which to evaluate the PDF.
        mean (float): The mean of the normal distribution.
        std_dev (float): The standard deviation of the normal distribution.
    
    Returns:
        float: The value of the PDF at x.
    """
    exponent = -((x - mean) ** 2) / (2 * (std_dev ** 2))
    pdf = (1 / (math.sqrt(2 * math.pi) * std_dev)) * math.exp(exponent)
    return pdf

# Example usage
x = 5
mean = 5
std_dev = 1

probability = normal_pdf(x, mean, std_dev)
print("Probability density at x =", x, ":", probability)
