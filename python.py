def calculator():
    print("This is a simple calculator")

    print("You are asked to enter a number")
    num1 = int(input())
    print("Enter second number")
    num2 = int(input())

    print("Choose an Operation")
    print("")

    print("1 = addition")
    print("2 = subtraction")
    print("3 = multiplication")
    print("4 = division")

    print("Choose the operation you would like to work with")
    operation = int(input())
    if operation == 1:
        print("your answer is", num1 + num2)
    elif operation == 2:
        print("your answeer is ", num1 - num2)
    elif operation == 3:
        print("your answer is ", num1 * num2)
    elif operation == 4:
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("ERROR")

    else:
        print("Invalid")

    print("Do you want to continue: ")     
    answer = "yes"
    if answer == "yes" :
        calculator()
calculator()                           
        

