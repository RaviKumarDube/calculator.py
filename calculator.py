num1=int(input("Enter the First number: "))#variable to store first number
num2=int(input("Enter the second number:"))#variable to store second number
operator=input(" Enter the operator(+,-,*,/):")#variable to store operator

match(operator):
    case '+':
        print(f"The sum of {num1} and {num2} is: {num1+num2}")
        exit()
    case '-':
        print(f"The difference of {num1} and {num2} is: {num1-num2}")
        exit()
    case '*':
        print(f"The product of {num1} and {num2} is: {num1*num2}")
        exit()
    case '/':    
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"The division of {num1} by {num2} is: {num1/num2}")
        exit()
    case _:
        print("Invalid operator. Please use +, -, *, or /.")
        exit()    