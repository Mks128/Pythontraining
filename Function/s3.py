import math
sqrt_value = math.sqrt(2)
print(f"The square root of 2 is: {sqrt_value}")


import os
cwd = os.getcwd()
print(f"The current working directory is: {cwd}")

files = os.listdir(cwd)
print(f"Files in the current directory: {files}")
for file in files:    print(file)