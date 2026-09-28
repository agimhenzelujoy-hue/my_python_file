first_number = int(input("Enter your first number: "))
operand = input("Enter the operand '*, +, /, -': ")
second_number = int(input("Enter second number: "))
if operand == "*":
    print(first_number * second_number)
elif operand == "+":
    print(first_number + second_number)
elif operand == "-":
    print(first_number - second_number)
elif operand == "/":
    if first_number == 0:
        print("Division by zero error")
    else:
        print(first_number / second_number)
else:
    print("Invalid operator")