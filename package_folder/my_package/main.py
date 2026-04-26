import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import my_package

result_add = my_package.add(5, 3)
result_subtract = my_package.subtract(5, 3)
result_multiply = my_package.multiply(5, 3)
print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")