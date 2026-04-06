import re
text = "Hello how are you \
My name is MKS\
Iam learning Python\
As Python is used for more in Devops Nowadays\
"
pattern = r"Python"
result =re.findall(pattern, text)
print(result)
