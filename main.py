# Get users input
print("1 - Addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")
option = int(input("choose an operation: "))
answer = 0

if "option in [1,2,3,4]" :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Perform operation based on user input
    if option == 1:
        answer = num1 + num2
    elif option == 2:
        answer = num1 - num2
    elif option == 3:
        answer = num1 * num2
    elif option == 4:
        answer = num1 // num2

    else:
        print("Invalid operation entered")

    print("The result of the operation is {}".format(answer))




