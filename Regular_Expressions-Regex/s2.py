import re
text = "hello world"
pattern = r"world"
result = re.search(pattern, text)
if result:
    print (result.group())