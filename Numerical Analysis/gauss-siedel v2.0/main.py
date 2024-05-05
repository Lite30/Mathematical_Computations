import menu

rows = 0
cols = 0
# Define 3x3 matrix A in Ax=b
A = None
# Define column vector B in Ax=b
B = None
# Initial guess x(0)
x0 = None

# Main program loop
while True:
    menu.menu()
    choice = input("Enter your choice (1-7):")

    if choice == '1':
        menu.option1()
    elif choice == '2':
        menu.option2()
    elif choice == '3':
        A = menu.option3(A)
    elif choice == '4':
        B = menu.option4(B)
    elif choice == '5':
        x0 = menu.option5(x0)
    elif choice == '6':
        menu.option6(A,B,x0)
    elif choice == '7':
        menu.option7()
        break
    else:
        print("\n+" + "-"*52 + "+")
        print("| Invalid choice. Please enter a number from 1 to 7. |")
        print("+" + "-"*52 + "+\n")