str="PYTHON"
str=str[::-1]
print(str)

def reverse_string(s):
    result=""
    for char in s:
        result=char+result
    return result
print(reverse_string("python")
