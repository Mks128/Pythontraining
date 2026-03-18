Dictionary = {"name":"Alice","age":25,"city":"New York"}
print (Dictionary["name"])
Dictionary["profession"] = "Engineer"
print ("The updated Dictionary is:", Dictionary)
Dictionary.update({"profession":"Teacher"})
print ("The updated Dictionary is:", Dictionary)
Dictionary.pop("profession")
print("The updated Dictionary is:", Dictionary)