import mymodule
name = input("Enter your name: ")
greeting = mymodule.greet(name)
print(greeting) 

result_add = mymodule.add(10, 5)
print(f"Addition: {result_add}")
result_subtract = mymodule.subtract(10, 5)
print(f"Subtraction: {result_subtract}")
result_multiply = mymodule.multiply(10, 5)
print(f"Multiplication: {result_multiply}")
result_divide = mymodule.divide(10, 5)
print(f"Division: {result_divide}")

