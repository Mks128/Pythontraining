import sys
print("Command-line arguments:", sys.argv)
# The first argument is the script name itself
script_name = sys.argv[0]
print("Script name:", script_name)
# Check if additional arguments are provided
if len(sys.argv) > 1:
    first_arg = sys.argv[1]
    print("First argument:", first_arg)
else:
    print("No additional arguments provided.")