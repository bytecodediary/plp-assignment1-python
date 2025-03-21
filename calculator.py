first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
arithmetic_operation = input("Enter the arithmetic operation you want to perform: ")

if arithmetic_operation == "+":
    result = first_number + second_number
    print(result)
elif arithmetic_operation == "-":
    result = first_number + second_number
    print(result)
elif arithmetic_operation == "*":
    result = first_number * second_number
    print(result)
elif arithmetic_operation == "/":
    try:
        result = first_number / second_number
        print(result)
    except ZeroDivisionError:
        print("division by zero not allowed")
else:
    print("Operation unknown")
