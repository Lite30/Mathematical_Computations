# Machine Problem: Straight Line Fitting

This repository contains code for a machine problem assignment from the Department of Mathematics and Computer Science at the National University of Lesotho. The assignment tasks are as follows:

1. Generate random data in 2D that approximate a straight line. Save it as a .csv file.
2. Based on the data generated above, design a model (a straight line: y = c + mx) which best fits that data using the gradient descent algorithm.
3. Illustrate, using Excel spreadsheet or any other similar tool, a scatter graph of the training data generated in step 1, and the straight line model determined in step 2.

## Files

- `gradient.py`: Python script containing the implementation of gradient descent.
- `points.py`: Python module containing functions for loading data from a CSV file and helper functions.
- `plot.py`: Python module containing functions for ploting the best fit using matplotlib
- `lite_data.csv`: CSV file containing randomly generated data points, which will be created upon running points.py.
  
## Instructions for Running the Code

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone this repository to your local machine or download the ZIP file.

3. Install the required Python libraries by running the following command in your terminal or command prompt:

    ```
    1. pip install numpy
    2. pip install matplotlib
    3. pip install pandas
    ```

4. Once the libraries are installed, navigate to the directory containing the code files.

5. Run the Python scripts by executing the following command:

    ```
    python points.py
    python gradient.py
    python plot.py
    ```

6. The scripts will generate random data, perform gradient descent to find the best-fit line, and plot the data along with the model.

7. You can adjust the parameters like the number of data points, learning rate, and iterations directly in the programs files.
8. Always make sure that the python files are in the same directory or folder



