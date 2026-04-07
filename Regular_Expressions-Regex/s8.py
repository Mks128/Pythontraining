import re
# Regular expression to capture lines with "WARNING" or "ERROR" 
pattern = r"(WARNING|ERROR)"
#path to the log file
log_file_path = "/var/log/system.log"
# Open the log file and read it line by line
with open(log_file_path, 'r') as log_file:
    for line in log_file:
        # Check if the line matches the pattern
        if re.search(pattern, line):
            print(line.strip())#Print the matching line without leading/trailing whitespace