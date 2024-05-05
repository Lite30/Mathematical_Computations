import functions 
def menu():
    print("+" + "-"*30 + "+")
    print("| Menu for GAUSS-SIEDEL METHOD |")
    print("+" + "-"*30 + "+")
    print("| 1. Enter number of columns   |")
    print("| 2. Enter number of rows      |")
    print("| 3. Enter value into matrix A |")
    print("| 4. Enter value into vector B |")
    print("| 5. Enter initial guess x0    |")
    print("| 6. Calculate                 |")
    print("| 7. Exit                      |")
    print("+" + "-"*30 + "+\n")


def option1():
    global cols
    print("+" + "-"*31 + "+")
    print("| You chose Option 1            |")
    print("+" + "-"*31 + "+")
    cols = int(input("Enter the number of columns: "))

def option2():
    global rows
    print("+" + "-"*31 + "+")
    print("| You chose Option 2            |")
    print("+" + "-"*31 + "+")
    rows = int(input("Enter the number of rows: "))

def option3(A):
    print("+" + "-"*31 + "+")
    print("| You chose Option 3            |")
    print("+" + "-"*31 + "+")
    A = functions.input_matrix(rows,cols)
    return A

def option4(B):
    print("+" + "-"*31 + "+")
    print("| You chose Option 4            |")
    print("+" + "-"*31 + "+")
    B = functions.np.array(functions.input_matrix(cols, 1))
    return B

def option5(x0):
    print("+" + "-"*31 + "+")
    print("| You chose Option 5            |")
    print("+" + "-"*31 + "+")
    x0 = functions.np.array(functions.input_matrix(cols, 1))
    return x0

def option6(A, B, x0):
    print("+" + "-"*31 + "+")
    print("| You chose Option 6            |")
    print("+" + "-"*31 + "+")
    if A is None or B is None or x0 is None:
        print("Please enter matrix dimensions and values first.")
    else:
        solution = functions.gauss_seidel(A, B, x0)
        print("Solution:", solution)

def option7():
    print("+" + "-"*31 + "+")
    print("| Exiting program...           |")
    print("+" + "-"*31 + "+")


