"""Exception handling handle error that may occur during program execution
try:block of code where exception might occur
except:catch and handle the exception
finally:always run whether an exception occured or not
"""
try:
    result=10/0
except ZeroDivisionError:
    print("you can not divisible by zero")
finally:
    print("execution completed")
    
    
try:
    x=int(input("enter the no: "))
    result=10/x
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("you can not divisible by zero") 

#raising Exception:you can raise exception manually usin raise

