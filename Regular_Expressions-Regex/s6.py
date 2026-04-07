#Using Regex to format Date of Birth as DD.MM.YYYY
import re

# Method 1: Extract date components and reformat using re.match() or re.search()
def format_dob_method1():
    # Input date in MM/DD/YYYY format
    dob_input = "06/15/1984"
    
    # Regex pattern to capture date components
    pattern = r'(\d{2})/(\d{2})/(\d{4})'
    match = re.match(pattern, dob_input)
    
    if match:
        month, day, year = match.groups()
        # Reformat to DD.MM.YYYY
        formatted_dob = f"{day}.{month}.{year}"
        print(f"Input: {dob_input} → Output: {formatted_dob}")

# Method 2: Using re.sub() for direct replacement and reordering
def format_dob_method2():
    # Input date in MM/DD/YYYY format
    dob_input = "06/15/1984"
    
    # Use re.sub() to swap the groups and change delimiter
    formatted_dob = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2.\1.\3', dob_input)
    print(f"Using re.sub(): {dob_input} → {formatted_dob}")

# Method 3: Handle different input formats
def format_dob_method3():
    dates = [
        "06/15/1984",      # MM/DD/YYYY
        "06-15-1984",      # MM-DD-YYYY
        "15-06-1984",      # DD-MM-YYYY (already in desired format)
    ]
    
    for date in dates:
        # Pattern to match various date formats
        match = re.search(r'(\d{1,2})[-/](\d{1,2})[-/](\d{4})', date)
        if match:
            part1, part2, year = match.groups()
            # Assuming MM/DD format, swap to DD.MM.YYYY
            formatted_dob = f"{part2}.{part1}.{year}"
            print(f"{date} → {formatted_dob}")

# Method 4: Validate and format in one step
def format_dob_method4():
    dob_input = "06/15/1984"
    
    # Pattern with validation (ensures valid month 01-12, day 01-31)
    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(\d{4})$'
    
    if re.match(pattern, dob_input):
        formatted_dob = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2.\1.\3', dob_input)
        print(f"Valid DOB formatted: {formatted_dob}")
    else:
        print("Invalid date format")

# Run the examples
print("=== Formatting Date of Birth as DD.MM.YYYY ===")
format_dob_method1()
format_dob_method2()
print("\nMethod 3 - Different input formats:")
format_dob_method3()
print("\nMethod 4 - With validation:")
format_dob_method4()    