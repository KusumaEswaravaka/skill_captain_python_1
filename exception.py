def divide_numbers(num1, num2):
    
    try:
        result = num1 / num2
        print(f"The result of division is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

num1 = 4
num2 = 0
divide_numbers(num1, num2)
