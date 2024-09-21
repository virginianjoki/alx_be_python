num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        result = num1 + num2
        print(f"the result is {result}.")
    case "-" :
        result = num1 - num2
        print(f"the result is {result}.")
    case "*":
        result = num1 * num2
        print(f"the result is {result}.")
    case "/":
        if num2 == 0:
            print("number cannot be divided by 0")
        else:    
            result = num1  / num2
            print(f"the result is {result}.")
    case _:
        print("invalid operation. Please choose from +, -, * , / ")
                   