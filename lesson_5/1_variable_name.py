from keyword import kwlist
from string import punctuation

def is_variable_valid(name):
    if name in kwlist:
        return False
    if " " in name:
        return False
    if  name[0].isdigit():
        return False
    if set(name) & set(punctuation.replace("_", "")):
        return False
    if name.lower() != name :
        return False
    if "__" in name:
        return False
    return True

print(is_variable_valid(input("Enter a variable name: ")))