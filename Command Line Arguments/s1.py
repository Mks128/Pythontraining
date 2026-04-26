import sys
def add (num1, num2):
    return num1 + num2
def subtract (num1, num2):
    return num1 - num2
def multiply (num1, num2):
    return num1 * num2
num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])
if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
else:
    print("Invalid operation")
    sys.exit(1)

print(f"Result: {result}") 