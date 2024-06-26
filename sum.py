
num1 = 4
num2 = 2

try:

      sum = num1 + num2
      print(f"Sum of two numbers: {sum}")


      subtraction = num1 - num2
      print(f"Result of subtraction: {subtraction}")


      product = num1 * num2
      print(f"Product of two numbers: {product}")


      quotient = num1 / num2
      print("Quotient of division:", (quotient))

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")















    
    
           