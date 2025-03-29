def calculator():
    # Get users input
    operation = input("Enter operation (+,-,*,/): ")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Perform operation based on user input
    if operation == "+":
        answer = num1 + num2
        operation = "addition"