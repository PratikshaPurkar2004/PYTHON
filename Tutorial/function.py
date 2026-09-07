#function is a small block of reusable code that perform a specific task


def greet(name):
    print(name)
greet("pratiksha")

def sum(a,b):
    print(a+b)
sum(3,5)


def reverse_str(str):
    print(str[::-1])
reverse_str("pratiksha")

def reverse_string(s):
    return''.join(reversed(s))
print("reversed string:",reverse_string("python"))

#jar print function use kela tr ditect function la call kraycha and jr return use kela tr print use kraycha


def reverse_string(s):
    print(''.join(reversed(s)))
reverse_string("java")
   
def num(n):
    if(n%2==0):
        print("even no")
    elif(n==0):
        print("no is zero")
    else:
        print("negative no")
num(13)  
