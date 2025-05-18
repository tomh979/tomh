from math import floor, ceil
import random
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operation = input("What operation? (+, -, *, /, %, pow, abs, floor, ceil,random): ").strip().lower()
if operation == '+':
    print(f"Addition: {x + y}")
elif operation == '-':
    print(f"Subtraction: {x - y}")
elif operation == '*':
    print(f"Multiplication: {x * y}")
elif operation == '/':
    if y == 0:
        print("Error: Division by zero!")
    else:
        print(f"Division: {x / y}")
elif operation == '%':
    if y == 0:
        print("Error: Modulus by zero!")
    else:
        print(f"Modulus: {x % y}")  
elif operation == 'pow':
    print(f"Power: {pow(x, y)}")
elif operation == 'abs':
    print(f"Absolute of {x}: {abs(x)}")
    print(f"Absolute of {y}: {abs(y)}")
elif operation == 'floor':
    print(f"Floor of {x}: {floor(x)}")
    print(f"Floor of {y}: {floor(y)}")
elif operation == 'ceil':
    print(f"Ceil of {x}: {ceil(x)}")
    print(f"Ceil of {y}: {ceil(y)}")
elif operation == 'random':
    low = int(min(x, y))
    high = int(max(x, y))
    rand_num = random.randint(low, high)
    print(f"Random integer between {low} and {high}: {rand_num}")
else:
    print("Invalid operation!")